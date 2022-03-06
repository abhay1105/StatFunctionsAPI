from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


from inference_calculator import norm_cdf_calc, one_group_mean_testing, one_group_prop_testing, two_group_mean_testing

####### RequestParser Method (through body)
# normal_distribution_calc_args = reqparse.RequestParser()
# normal_distribution_calc_args.add_argument("mean", type = str, help = "Enter a valid quantity", required = True)
# normal_distribution_calc_args.add_argument("standard_deviation", type = str, help = "Enter a valid quantity", required = True)
# normal_distribution_calc_args.add_argument("lower_bound", type = str, help = "Enter a valid quantity", required = True)
# normal_distribution_calc_args.add_argument("upper_bound", type = str, help = "Enter a valid quantity", required = True)

class NormalDistributionCalc(Resource):
    def get(self, mean, stdDev, lowerBound, upperBound):
        area = norm_cdf_calc(mean, stdDev, lowerBound, upperBound)
        return {
            "area": area
        }

class OneGroupMeanTest(Resource):
    def get(self, sample_mean, sample_size, pop_mean, num_sided, alpha_level, std_dev, std_dev_type, norm_dist, rand_samp):
        solution = one_group_mean_testing(sample_mean, sample_size, pop_mean, num_sided, alpha_level, std_dev, std_dev_type, norm_dist, rand_samp)
        return {
            "solution": solution
        }

class TwoGroupMeanTest(Resource):
    def get(self, sample_mean_1, sample_std_1, sample_size_1, sample_mean_2, sample_std_2, sample_size_2, diff_mean, num_sided, alpha_level, ind_dist, rand_samp):
        solution = two_group_mean_testing(sample_mean_1, sample_std_1, sample_size_1, sample_mean_2, sample_std_2, sample_size_2, diff_mean, num_sided, alpha_level, ind_dist, rand_samp)
        return {
            "solution": solution
        }

class OneGroupPropTest(Resource):
    def get(self, sample_prop, sample_size, pop_prop, pop_size, num_sided, alpha_level, rand_samp):
        solution = one_group_prop_testing(sample_prop, sample_size, pop_prop, pop_size, num_sided, alpha_level, rand_samp)
        return {
            "solution": solution
        }

api.add_resource(NormalDistributionCalc, "/norm_dist_calc/mean=<string:mean>&stdDev=<string:stdDev>&lowerBound=<string:lowerBound>&upperBound=<string:upperBound>")
api.add_resource(OneGroupMeanTest, "/one_group_mean_test/sampleMean=<string:sample_mean>&sampleSize=<string:sample_size>&populationMean=<string:pop_mean>&numSided=<string:num_sided>&alphaLevel=<string:alpha_level>&standardDeviation=<string:std_dev>&standardDeviationType=<string:std_dev_type>&normallyDistributed=<string:norm_dist>&isRandom=<string:rand_samp>")
api.add_resource(TwoGroupMeanTest, "/two_group_mean_test/sampleMean1=<string:sample_mean_1>&sampleStandardDeviation1=<string:sample_std_1>&sampleSize1=<string:sample_size_1>&sampleMean2=<string:sample_mean_2>&sampleStandardDeviation2=<string:sample_std_2>&sampleSize2=<string:sample_size_2>&meanDifference=<string:diff_mean>&numSided=<string:num_sided>&alphaLevel=<string:alpha_level>&independentPopulations=<string:ind_dist>&isRandom=<string:rand_samp>")
api.add_resource(OneGroupPropTest, "/one_group_prop_test/sampleProportion=<string:sample_prop>&sampleSize=<string:sample_size>&populationProportion=<string:pop_prop>&populationSize=<string:pop_size>&numSided=<string:num_sided>&alphaLevel=<string:alpha_level>&isRandom=<string:rand_samp>")


if __name__ == "__main__":
    app.run(debug = True)