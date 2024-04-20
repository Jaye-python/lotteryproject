from django.shortcuts import render
import itertools
import random
import itertools
import multiprocessing


def home(request):
    return render(request, 'lotapp/home.html')

def get_potential_winning(data, prices, jackpot):
    base_price = prices.get(data[1][0], 0)
    if not base_price:
        return None
    sharing = {5: 1, 4: 1, 3: 0.6, 2: 0.6*0.5}
    winning = jackpot if data[0] == 5 else base_price * sharing.get(data[0], 0)
    return [*data, int(winning)]

def search_number_occurrences(numlist1: list, numlist2: list, number_of_match_limit=3) -> int:
    match_count = 0
    for number in numlist1:
        if number in numlist2[1]:
            match_count += 1
    return match_count if match_count > (number_of_match_limit - 1) else False


def process_combination(combo, plays, line_prices, jackpot_amount, rtp):
    occurences = [search_number_occurrences(combo, user_play, 2) for user_play in plays]
    play_occurences = [(occurrence, user_play) for occurrence, user_play in zip(occurences, plays) if occurrence]
    play_occurences_with_amount = [get_potential_winning(played, line_prices, jackpot_amount) for played in play_occurences]
    total_sum = sum(ocurrence[-1] for ocurrence in play_occurences_with_amount if ocurrence is not None)
    
    if total_sum == 0 or rtp / total_sum < 4:
        return None
    
    has_jkpt = any(x[0] == 5 for x in play_occurences_with_amount)
    match = total_sum / rtp * 100
    winners = len(play_occurences)
    
    return {
        'match': match,
        'winners': winners,
        'combo': combo,
        'has_jkpt': has_jkpt,
    }

class SalaryForLifeDraw:
    @staticmethod
    def draw(plays, rtp, line_prices, jackpot_amount, jackpot=False) -> dict:
        num_plays = 5000
        num_cores = multiprocessing.cpu_count()
        
        random_combos = random.sample(list(itertools.combinations(range(1, 50), 5)), num_plays)
        
        with multiprocessing.Pool(num_cores) as pool:
            results = [pool.apply_async(process_combination, args=(combo, plays, line_prices, jackpot_amount, rtp)) for combo in random_combos]
            results = [res.get() for res in results]
        
        best_match_info = max((result for result in results if result is not None), key=lambda x: x['match'], default=None)
        best_match_with_jkpt = max((result for result in results if result is not None and result['has_jkpt']), key=lambda x: x['match'], default=None)
        best_match_witho_jkpt = max((result for result in results if result is not None and not result['has_jkpt']), key=lambda x: x['match'], default=None)
        
        return {
            'best_match': best_match_info['match'] if best_match_info else 0,
            'best_match_combo': best_match_info['combo'] if best_match_info else [],
            'best_match_with_jkpt': best_match_with_jkpt['match'] if best_match_with_jkpt else 0,
            'best_match_with_jkpt_combo': best_match_with_jkpt['combo'] if best_match_with_jkpt else [],
            'best_match_witho_jkpt': best_match_witho_jkpt['match'] if best_match_witho_jkpt else 0,
            'best_match_witho_jkpt_combo': best_match_witho_jkpt['combo'] if best_match_witho_jkpt else [],
        }

