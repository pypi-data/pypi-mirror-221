from scipy import stats 
from statsmodels.sandbox.stats.multicomp import multipletests
import numpy as np
import pandas as pd
import collections as col

def has_hpo(pat, hpo, all_hpo):
    if not isinstance(all_hpo, col.defaultdict):
        for h in pat.phenotype_ids:
            if h == hpo:
                return True
        return False
    else:
        for h in pat.phenotype_ids:
            if h in all_hpo.get(hpo):
                return True
        return False

def group_similar_hpos(hpo_total_list, hpo_short_list):
    hpo_grouping = col.defaultdict(list)
    skip_done_hpos = []
    for hpo_id in hpo_short_list:
        if hpo_id not in skip_done_hpos:
            similar_hpos = [[hpo_id, len(hpo_total_list[hpo_id].list_ancestors())]]
            grouping_list = hpo_total_list[hpo_id].list_descendants() + hpo_total_list[hpo_id].list_ancestors()
            for hpo_id2 in hpo_total_list.keys():
                if hpo_id2 in grouping_list:
                    similar_hpos.append([hpo_id2, len(hpo_total_list[hpo_id2].list_ancestors())])
            smallest = ['tempID', 1000000]
            for hpo_id3 in similar_hpos:
                if int(hpo_id3[1]) < int(smallest[1]):
                    smallest = hpo_id3
                elif int(hpo_id3[1]) == int(smallest[1]):
                    raise ValueError(f"ERROR: {hpo_id3[0]} and {smallest[0]} are at the same level with {hpo_id3[1]} ancestors each.")
            hpo_grouping[smallest[0]] = [ids[0] for ids in similar_hpos]
            skip_done_hpos.extend([ids[0] for ids in similar_hpos])
    return hpo_grouping

def run_stats(  cohort, Fun1, Fun2, extraVar_1, extraVar_2, 
                percent_patients = 10, adjusted_pval_method = 'fdr_bh', include_descendants = False): 
    """ Runs the Genotype-Phenotype Correlation calculations

    Args:
        cohort (Cohort) :   Cohort Class, collection of all Patients 
                            be considered for this correlation

        Fun1 & Fun2 (function) :    Any function listed below. Will be the 
                                    correlation test.
                                Options - is_var_match, is_not_var_match, is_var_type, 
                                is_not_var_type, in_feature, not_in_feature

        extraVar_1 & extraVar_2 (String) :  The variable needed to run each 
                                            function above respectively. 

    Optional Args:
        percent_patients (Integer - 10) :   The threshold for the least amount of 
                                            patients to have a specific HPO for the
                                            HPO to still be considered for testing.

        adjusted_pval_method (String - 'fdr_bh') :  Method for the adjusted p-value. 
                                Options - bonferroni, sidak, hold-sidak, holm, simes-hochberg,
                                hommel, fdr_bh, fdr_by, fdr_tsbh, fdr_tsbky

    Returns:
        DataFrame : A pandas DataFrame of the results. 
                    Columns - 
                    '1 w/ hpo' - Total Patients with HPO and who return True with Fun1
                    '1 w/o hpo' - Total Patients without HPO and who return True with Fun1
                    '2 w/ hpo' - Total Patients with HPO and who return True with Fun2
                    '2 w/o hpo' - Total Patients without HPO and who return True with Fun2
                    'pval' - Unadjusted p-value after Fisher-Exact test
                    'adjusted pval' - p-value after adjusted_pval_method adjusted it
    
    """
    hpo_counts = cohort.count_patients_per_hpo()
    all_hpo = []
    for row in hpo_counts.iterrows():
        if row[1].at['Percent'] >= (percent_patients/100):
            all_hpo.append(row[0])
    if len(all_hpo) == 0:
        raise ValueError(f'No HPO term is present in over {percent_patients}% of the patients.')
    print(f"Total hpo terms: {all_hpo}")
    if include_descendants:
        all_hpo = group_similar_hpos(cohort.all_phenotypes, all_hpo)
    allSeries = []
    for hpo_id in all_hpo:
        ## Count patients that have hpo_id and skip test if under certain percent of patients have it
        ## Create a new class to do these tests on hpo_ids, also check for patients who are related 
        var1_with_hpo = len([ pat for pat in cohort.all_patients.values() if has_hpo(pat, hpo_id, all_hpo) and Fun1(pat, extraVar_1)])
        var1_without_hpo = len([ pat for pat in  cohort.all_patients.values() if not has_hpo(pat, hpo_id, all_hpo) and Fun1(pat,extraVar_1)])
        var2_with_hpo = len([ pat  for pat in cohort.all_patients.values() if has_hpo(pat, hpo_id, all_hpo) and Fun2(pat,extraVar_2)])
        var2_without_hpo = len([ pat for pat in cohort.all_patients.values() if not has_hpo(pat, hpo_id, all_hpo) and Fun2(pat,extraVar_2)])
        table = np.array([[var1_with_hpo, var1_without_hpo], [var2_with_hpo, var2_without_hpo]])
        oddsr, p =  stats.fisher_exact(table, alternative='two-sided') 
        allSeries.append(pd.Series([var1_with_hpo, var1_without_hpo, var2_with_hpo, var2_without_hpo, p], name= hpo_id + ' - ' + hpo_counts.at[hpo_id, 'Class'].label, index=['1 w/ hpo', '1 w/o hpo', '2 w/ hpo', '2 w/o hpo', 'pval']))
    results = pd.concat(allSeries, axis=1)
    results = results.transpose()
    results = results.sort_values(['pval'])
    pval_adjusted = multipletests(results['pval'].to_list(), alpha=0.05, method=adjusted_pval_method) 
    results['adjusted pval'] = np.array(pval_adjusted[1])
    
    return results

        