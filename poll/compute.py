from poll import models
import time
import random


def chunked_result(pk):
    yield '<pre>Thank you for triggering the RESULT CALCULATION function.\n'
    yield 'Please wait while the result is being calculated.\n'
    yield ' ' * 1024
    yield '\n'
    time.sleep(1)

    poll = models.Poll.objects.get(id=pk)
    candidates = poll.candidate_set.all()
    candidates = {c.id: c.title for c in candidates}
    yield 'There were {} candidates:\n'.format(len(candidates))
    for id in candidates:
        yield '{}: {}\n'.format(id, candidates[id])
    votes = poll.vote_set.all()
    yield '\nA total of {} votes were cast.\n'.format(votes.count())
    for vote in votes:
        yield 'On {}, user {} voted: {}\n'.format(
             str(vote.submitted)[:16],
             vote.get_username(),
             vote.ranked_choices,
            )
    yield '\n'
    num_seats = 5
    yield 'Using num_seats: {}\n'.format(num_seats)
    yield 'Initial Droop quota: {:.2f}\n'.format(droop(len(votes), num_seats))

    yield 'This could take a while...\n'

    result = yield from compute(votes, candidates, num_seats)
    
    yield '</pre>'
    yield '<br/><a href="/v/{}">Return to poll</a>'.format(pk)



def compute(votes, candidates, num_seats):
    yield 'Starting compute function...\n'
    
    yield 'Setting initial state: all candidates hopeful, weights 1.\n\n'
    weights = {id: 1 for id in candidates}

    round = 1
    done_electing = False
    num_remaining = len(candidates)

    while not done_electing:
        weighting = 1
        done_reweighting = False
        while not done_reweighting:
            yield '\nRound {}, weighting {}: Tallying current totals by weight...\n'.format(round, weighting)
            (tallies, excess) = yield from tally(votes, weights)
        
            for id in sorted(tallies, key=tallies.get, reverse=True):
                if weights[id] > 0:
                    yield '{:.2f} votes (weight={:.4f}) for {}: {}\n'.format(tallies[id], weights[id], id, candidates[id])
        
            yield '{:.2f} excess votes due to exhausted ballots\n'.format(excess)
        
            droop_mod = droop((len(votes) - excess), num_seats)
            num_elected = len([id for id in tallies if tallies[id] >= droop_mod])
            yield 'Modified droop quota={:.2f}, met by {} candidates\n'.format(droop_mod, num_elected)
    
            #optimistically, maybe we're done reweighting?
            done_reweighting = True
            for id in tallies:
                if tallies[id] > droop_mod + 0.01:
                    weights[id] *= (droop_mod / tallies[id])
                    yield 'Candidate {} weight reduced to {:.4f}\n'.format(id, weights[id])
                    # nope. need another go.
                    done_reweighting = False
            weighting += 1

        if num_elected >= num_seats:
            done_electing = True
            yield 'DONE ELECTING AND ALL MET MODIFIED QUOTA!'
        elif num_remaining <= num_seats:
            done_electing = True
            yield 'DONE ELECTING BECAUSE ONLY {} CANDIDATES REMAIN'.format(num_remaining)
        else:
            # time to eliminate a candidate
            worst_tally = min([tallies[id] for id in weights if weights[id] > 0])
            worst_candidates = [id for id in tallies if tallies[id] == worst_tally and weights[id] > 0]
            if len(worst_candidates) > 1:
                yield 'Randomly choosing a candidate to eliminate, from among {}\n'.format(worst_candidates)
            to_eliminate = random.choice(worst_candidates)
            yield 'ELIMINATING candidate {}: {}\n'.format(to_eliminate, candidates[to_eliminate])
            weights[to_eliminate] = 0.0
            num_remaining -= 1
            yield 'There are now {} candidates remaining\n'.format(num_remaining)
            round += 1
            yield '\n============\n'

    return tallies


def tally(votes, weights):
    tallies = {id: 0.0 for id in weights}
    excess = 0.0
    for vote in votes:
        remaining_value = 1.0
        choices = vote.ranked_choices.split(',')
        for choice in choices:
            try:
                choice = int(choice)
                choice_value = remaining_value * weights[choice]
            except:
                yield 'Skipping invalid choice {} in vote {}\n'.format(choice, vote.id)
                continue
            tallies[choice] += choice_value
            remaining_value -= choice_value
            if remaining_value == 0.0:
                break
        excess += remaining_value
    return (tallies, excess)

def droop(num_votes, num_seats):
    return (float(num_votes) / (float(num_seats) + 1.0)) + 0.01
