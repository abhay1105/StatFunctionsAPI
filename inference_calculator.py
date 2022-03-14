# Conducts hypothesis testing procedures for different statistical scenarios
# Stat-O-Sphere


import distutils
import distutils.util


digits_rounded = 6

# function to convert to superscript
def get_super(x):
	normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
	super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
	res = x.maketrans(''.join(normal), ''.join(super_s))
	return x.translate(res)

# display superscipt
# print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ

# function to convert to subscript
def get_sub(x):
	normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
	sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
	res = x.maketrans(''.join(normal), ''.join(sub_s))
	return x.translate(res)

# display subscript
# print('H{}SO{}'.format(get_sub('2'),get_sub('4'))) #H₂SO₄


from scipy.stats import norm
from scipy.stats import t


def norm_cdf_calc(mean, std_dev, lower_bound, upper_bound):
    mean = float(mean)
    std_dev = float(std_dev)
    prob = 0
    if lower_bound == "NONE":
        upper_bound = float(upper_bound)
        prob = norm(loc = mean, scale = std_dev).cdf(upper_bound)
    elif upper_bound == "NONE":
        lower_bound = float(lower_bound)
        prob = 1 - norm(loc = mean, scale = std_dev).cdf(lower_bound)
    else:
        upper_bound = float(upper_bound)
        lower_bound = float(lower_bound)
        prob = norm(loc = mean, scale = std_dev).cdf(upper_bound) - norm(loc = mean, scale = std_dev).cdf(lower_bound)
    return round(prob, digits_rounded)

def t_cdf_calc(df, lower_bound, upper_bound):
    df = float(df)
    prob = 0
    if lower_bound == "NONE":
        upper_bound = float(upper_bound)
        prob = t.cdf(x = upper_bound, df = df, loc = 0, scale = 1)
    elif upper_bound == "NONE":
        lower_bound = float(lower_bound)
        prob = 1 - t.cdf(x = lower_bound, df = df, loc = 0, scale = 1)
    else:
        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
        prob = t.cdf(x = upper_bound, df = df, loc = 0, scale = 1) - t.cdf(x = lower_bound, df = df, loc = 0, scale = 1)
    return round(prob, digits_rounded)


def checkNumSided(num_sided):
    num_sided = num_sided.lower()
    if "greater" in num_sided:
        num_sided = "greater_one_sided"
    elif "less" in num_sided:
        num_sided = "less_one_sided"
    else:
        num_sided = "two_sided"
    return num_sided

def checkStandardDeviationType(std_dev_type):
    print(std_dev_type.lower())
    return std_dev_type.lower()


def one_group_mean_testing(sample_mean, sample_size, pop_mean, num_sided, alpha_level, std_dev, std_dev_type, norm_dist, rand_samp):

    # General steps for 1-sample z-test for means:
        # Formulate the null and alternative hypotheses (one-sided or two-sided)
        # Establish alpha level
        # Identify which test to use (z-test for known sigma, t-test for unknown sigma)
        # Verify conditions for test:
            # Normally distributed population
            # The sample is a simple random sample
            # Population standard deviation is known
        # Conduct the test
        # State statistical signifigance conclusion

    # General steps for 1-sample t-test for means:
        # Formulate the null and alternative hypotheses (one-sided or two-sided)
        # Establish alpha level
        # Identify which test to use (z-test for known sigma, t-test for unknown sigma)
        # Verify conditions for test:
            # Normally distributed population (Not necessarily, proven by CLT instead)
            # The sample is a simple random sample
            # Sample is at least 30 large (according to Central Limit Theorem [CLT])
        # Conduct the test
        # State statistical signifigance conclusion

    # convert variable types
    sample_mean = float(sample_mean)
    sample_size = float(sample_size)
    pop_mean = float(pop_mean)
    alpha_level = float(alpha_level)
    std_dev = float(std_dev)
    norm_dist = bool(distutils.util.strtobool(norm_dist))
    rand_samp = bool(distutils.util.strtobool(rand_samp))

    # convert string variables
    num_sided = checkNumSided(num_sided)
    std_dev_type = checkStandardDeviationType(std_dev_type)

    # determine test type
    test_type = ""
    if std_dev_type == "population":
        test_type = "1-Sample Z-Test for Means"
        print("reached here")
    else:
        test_type = "1-Sample T-Test for Means"
        print("reached here 2")

    # verify conditions for test
    if norm_dist == False:
        return "The population from which this sample is obtained from is not normally distributed."
    if rand_samp == False:
        return "The sample is not a simple random sample."

    # formulate null and alternate hypotheses
    null_hypothesis = "Null: μ" + get_sub(str(0)) + " = " + str(pop_mean)
    null_hypothesis_desc = "The sample is from a population with a mean of " + str(pop_mean) + "."

    alt_hypothesis = "Alternate: μ" + get_sub("a") + " "
    alt_hypothesis_desc = ""

    if num_sided == "less_one_sided":
        alt_hypothesis += "< " + str(pop_mean)
        alt_hypothesis_desc = "The sample is from a population with a mean less than " + str(pop_mean) + "."
    elif num_sided == "greater_one_sided":
        alt_hypothesis += "> " + str(pop_mean)
        alt_hypothesis_desc = "The sample is from a population with a mean greater than " + str(pop_mean) + "."
    else:
        alt_hypothesis += "≠ " + str(pop_mean)
        alt_hypothesis_desc = "The sample is from a population with a mean not equal to " + str(pop_mean) + "."

    # establish alpha level
    alpha_level_desc = "The alpha level is " + str(alpha_level) + "."

    # conduct test
    prob = 0
    prob_desc = ""
    if test_type == "1-Sample Z-Test for Means":
        z_score = abs(round((sample_mean - pop_mean) / (std_dev / (sample_size ** 0.5)), digits_rounded))
        prob = norm_cdf_calc(0, 1, z_score, "NONE")
        if num_sided == "two_sided":
            prob *= 2
    else:
        t_score = abs(round((sample_mean - pop_mean) / (std_dev / (sample_size ** 0.5)), digits_rounded))
        prob = t_cdf_calc(sample_size - 1, t_score, "NONE")
        if num_sided == "two_sided":
            prob *= 2
    prob_desc = "The calculated p-value is " + str(prob) + "."

    # state the conclusion
    conc = ""
    if prob <= alpha_level:
        conc = "Since the p-value, " + str(prob) + ", is less than or equal to the signifigance level, " + str(alpha_level) + ", there is sufficient evidence to reject the null hypothesis."
    else:
        conc = "Since the p-value, " + str(prob) + ", is greater than the signifigance level, " + str(alpha_level) + ", there is not sufficient evidence to reject the null hypothesis."

    # print the final step-by-step procedure
    final_doc = ""
    test_type_desc = ""
    conditions_desc = ""
    if test_type == "1-Sample Z-Test for Means":
        test_type_desc = "Since the population standard deviation is known in this scenario, the \"" + test_type + "\" can be used for this procedure."
    else:
        test_type_desc = "Since the population standard deviation is unknown in this scenario, the \"" + test_type + "\" will be used for this procedure."
    final_doc += test_type_desc + "\n\n"

    conditions_desc = "All of the following conditions have been verified to use this statistical test:\n-- A normally distributed population\n-- A simple random sample"
    final_doc += conditions_desc + "\n\n"

    final_doc += "Stating the hypotheses:\n\n"
    final_doc += null_hypothesis + "\n" + null_hypothesis_desc + "\n\n"
    final_doc += alt_hypothesis + "\n" + alt_hypothesis_desc + "\n\n"

    final_doc += alpha_level_desc + "\n\n"

    # add latex code to show formula

    final_doc += prob_desc + "\n\n"

    final_doc += conc

    return(final_doc)

def two_group_mean_testing(sample_mean_1, sample_std_1, sample_size_1, sample_mean_2, sample_std_2, sample_size_2, diff_mean, num_sided, alpha_level, ind_dist, rand_samp):

    # General steps for 2-sample t-test for means:
        # Formulate the null and alternative hypotheses (one-sided or two-sided)
        # Establish alpha level
        # Identify which test to use (2-Sample T-Test for Means)
        # Verify conditions for test:
            # Independent, distinct populations
            # The samples are both simple random samples
            # Population standard deviation is unknown for both
            # The combined sample size is above 30 (CLT)
        # Conduct the test
        # State statistical signifigance conclusion

    # convert variable types
    sample_mean_1 = float(sample_mean_1)
    sample_std_1 = float(sample_std_1)
    sample_size_1 = float(sample_size_1)
    sample_mean_2 = float(sample_mean_2)
    sample_std_2 = float(sample_std_2)
    sample_size_2 = float(sample_size_2)
    diff_mean = float(diff_mean)
    alpha_level = float(alpha_level)
    ind_dist = bool(distutils.util.strtobool(ind_dist))
    rand_samp = bool(distutils.util.strtobool(rand_samp))

    # convert string variables
    num_sided = checkNumSided(num_sided)

    # determine test type
    test_type = "2-Sample T-Test for Difference of Means"

    # verify conditions for test
    if ind_dist == False:
        return "The populations from which these sample are obtained from are not independent, distinct populations."
    if rand_samp == False:
        return "The obtained samples are not simple random samples."
    if sample_size_1 + sample_size_2 < 30:
        return "The combined size of both samples are not sufficient enough to satisfy the Central Limit Theorem."

    # formulate null and alternate hypotheses
    null_hypothesis = "Null: μ" + get_sub("1") + " - μ" + get_sub("2") + " = " + str(diff_mean)
    null_hypothesis_desc = ""
    if diff_mean == 0:
        null_hypothesis_desc = "There is no difference between the means of both distinct populations."
    else:
        null_hypothesis_desc = "The means of both distinct populations have a difference of " + str(diff_mean) + "."

    alt_hypothesis = "Alternate: μ" + get_sub("1") + " - μ" + get_sub("2") + " "
    alt_hypothesis_desc = ""

    if num_sided == "less_one_sided":
        alt_hypothesis += "< " + str(diff_mean)
        alt_hypothesis_desc = "The difference between both distinct populations is less than " + str(diff_mean) + "."
        if diff_mean == 0:
            alt_hypothesis_desc = "The mean of population 2 is greater than the mean of population 1."
    elif num_sided == "greater_one_sided":
        alt_hypothesis += "> " + str(diff_mean)
        alt_hypothesis_desc = "The difference between both distinct populations is greater than " + str(diff_mean) + "."
        if diff_mean == 0:
            alt_hypothesis_desc = "The mean of population 1 is greater than the mean of population 2."
    else:
        alt_hypothesis += "≠ " + str(diff_mean)
        alt_hypothesis_desc = "The difference between both distinct populations is not " + str(diff_mean) + "."
        if diff_mean == 0:
            alt_hypothesis_desc = "The mean of population 1 is not the same as the mean of population 2."

    # establish alpha level
    alpha_level_desc = "The alpha level is " + str(alpha_level) + "."

    # conduct test
    num = (sample_mean_1 - sample_mean_2) - diff_mean
    denom = (((sample_std_1 ** 2) / sample_size_1) + ((sample_std_2 ** 2) / sample_size_2)) ** 0.5
    t_score = abs(round(num / denom, digits_rounded))
    df = 0
    if sample_size_1 <= sample_size_2:
        df = sample_size_1 - 1
    else:
        df = sample_size_2 - 1
    prob = t_cdf_calc(df, t_score, "NONE")
    if num_sided == "two_sided":
        prob *= 2
    prob_desc = "The calculated p-value is " + str(prob) + "."

    # state the conclusion
    conc = ""
    if prob <= alpha_level:
        conc = "Since the p-value, " + str(prob) + ", is less than or equal to the signifigance level, " + str(alpha_level) + ", there is sufficient evidence to reject the null hypothesis."
    else:
        conc = "Since the p-value, " + str(prob) + ", is greater than the signifigance level, " + str(alpha_level) + ", there is not sufficient evidence to reject the null hypothesis."

    # print the final step-by-step procedure
    final_doc = ""
    
    test_type_desc = "Since the difference in means between two populations is being observed in this scenario, the \"" + test_type + "\" can be used for this procedure."
    final_doc += test_type_desc + "\n\n"

    conditions_desc = "All of the following conditions have been verified to use this statistical test:\n-- Samples from independent, distinct populations\n-- Samples are simple random samples\n-- The combined sample size is above 30 (to satisfy the Central Limit Theorem)"
    final_doc += conditions_desc + "\n\n"

    final_doc += "Stating the hypotheses:\n\n"
    final_doc += null_hypothesis + "\n" + null_hypothesis_desc + "\n\n"
    final_doc += alt_hypothesis + "\n" + alt_hypothesis_desc + "\n\n"

    final_doc += alpha_level_desc + "\n\n"

    # add latex code to show formula

    final_doc += prob_desc + "\n\n"

    final_doc += conc

    return(final_doc)

def one_group_prop_testing(sample_prop, sample_size, pop_prop, pop_size, num_sided, alpha_level, rand_samp):

    # General steps for 1-sample z-test for proportions:
        # Formulate the null and alternative hypotheses (one-sided or two-sided)
        # Establish alpha level
        # Identify which test to use (1-Sample Z-Test for Proportions)
        # Verify conditions for test:
            # To be considered binomial: N greater than or equal to 10 n
            # The sample is a simple random sample
            # Expected number of successes and failures is at least 10
        # Conduct the test
        # State statistical signifigance conclusion

    # convert variable types
    sample_prop = float(sample_prop)
    sample_size = float(sample_size)
    pop_prop = float(pop_prop)
    pop_size = float(pop_size)
    alpha_level = float(alpha_level)
    rand_samp = bool(distutils.util.strtobool(rand_samp))

    # convert string variables
    num_sided = checkNumSided(num_sided)

    # determine test type
    test_type = "1-Sample Z-Test for Proportions"

    # verify conditions for test
    if pop_size < (10 * sample_size):
        return "The population from which this sample is drawn from is not large enough for it to be considered binomial."
    if rand_samp == False:
        return "The sample is not a simple random sample."
    if ((sample_size * pop_prop) < 10) or ((sample_size * (1 - pop_prop)) < 10):
        return "The normal approximation of the binomial cannot be used since the expected number of successes and/or failures is below 10."

    # formulate null and alternate hypotheses
    null_hypothesis = "Null: p" + get_sub(str(0)) + " = " + str(pop_prop)
    null_hypothesis_desc = "The sample is from a population with a proportion of " + str(pop_prop) + "."

    alt_hypothesis = "Alternate: p" + get_sub("a") + " "
    alt_hypothesis_desc = ""

    if num_sided == "less_one_sided":
        alt_hypothesis += "< " + str(pop_prop)
        alt_hypothesis_desc = "The sample is from a population with a proportion less than " + str(pop_prop) + "."
    elif num_sided == "greater_one_sided":
        alt_hypothesis += "> " + str(pop_prop)
        alt_hypothesis_desc = "The sample is from a population with a proportion greater than " + str(pop_prop) + "."
    else:
        alt_hypothesis += "≠ " + str(pop_prop)
        alt_hypothesis_desc = "The sample is from a population with a proportion not equal to " + str(pop_prop) + "."

    # establish alpha level
    alpha_level_desc = "The alpha level is " + str(alpha_level) + "."

    # conduct test
    z_score = abs(round((sample_prop - pop_prop) / (((pop_prop * (1 - pop_prop)) / sample_size) ** 0.5), digits_rounded))
    prob = norm_cdf_calc(0, 1, z_score, "NONE")
    if num_sided == "two_sided":
        prob *= 2
    prob_desc = "The calculated p-value is " + str(prob) + "."

    # state the conclusion
    conc = ""
    if prob <= alpha_level:
        conc = "Since the p-value, " + str(prob) + ", is less than or equal to the signifigance level, " + str(alpha_level) + ", there is sufficient evidence to reject the null hypothesis."
    else:
        conc = "Since the p-value, " + str(prob) + ", is greater than the signifigance level, " + str(alpha_level) + ", there is not sufficient evidence to reject the null hypothesis."

    # print the final step-by-step procedure
    final_doc = ""

    test_type_desc = "Since the proportion of a population is being observed here, the \"" + test_type + "\" can be used for this procedure."
    final_doc += test_type_desc + "\n\n"

    conditions_desc = "All of the following conditions have been verified to use this statistical test:\n-- A sample drawn from a significantly larger population\n-- A simple random sample\n-- The expected number of successes and failures is above 10"
    final_doc += conditions_desc + "\n\n"

    final_doc += "Stating the hypotheses:\n\n"
    final_doc += null_hypothesis + "\n" + null_hypothesis_desc + "\n\n"
    final_doc += alt_hypothesis + "\n" + alt_hypothesis_desc + "\n\n"

    final_doc += alpha_level_desc + "\n\n"

    # add latex code to show formula

    final_doc += prob_desc + "\n\n"

    final_doc += conc

    return(final_doc)
