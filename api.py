from flask import Flask, request, json
from inference_calculator import norm_cdf_calc, one_group_mean_testing, two_group_mean_testing, one_group_prop_testing


app = Flask(__name__)

def verify_json(request):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        return request.json
    else:
        return 'Content-Type not supported!'

def process_json(request):
    return json.loads(request.data)

@app.route('/test', methods=['GET'])
def test():
    return {
        "message": "API IS RECIEVING REQUESTS"
    }

@app.route('/norm_dist_calc', methods=['POST'])
def norm_dist_calc():
    data = request.get_json()
    area = norm_cdf_calc(
        mean = data["mean"],
        std_dev = data["std_dev"],
        lower_bound = data["lower_bound"],
        upper_bound = data["upper_bound"]
    )
    return {
        "area": area
    }

@app.route('/one_group_mean_test', methods=['POST'])
def one_group_mean_test():
    data = request.get_json()
    solution = one_group_mean_testing(
        sample_mean = data["sample_mean"],
        sample_size = data["sample_size"],
        pop_mean = data["pop_mean"],
        num_sided = data["num_sided"],
        alpha_level = data["alpha_level"],
        std_dev = data["std_dev"],
        std_dev_type = data["std_dev_type"],
        norm_dist = data["norm_dist"],
        rand_samp = data["rand_samp"]
    )
    return {
        "solution": solution
    }

@app.route('/two_group_mean_test', methods=['POST'])
def two_group_mean_test():
    data = request.get_json()
    solution = two_group_mean_testing(
        sample_mean_1 = data["sample_mean_1"],
        sample_std_1 = data["sample_std_1"],
        sample_size_1 = data["sample_size_1"],
        sample_mean_2 = data["sample_mean_2"],
        sample_std_2 = data["sample_std_2"],
        sample_size_2 = data["sample_size_2"],
        diff_mean = data["diff_mean"],
        num_sided = data["num_sided"],
        alpha_level = data["alpha_level"],
        ind_dist = data["ind_dist"],
        rand_samp = data["rand_samp"]
    )
    return {
        "solution": solution
    }

@app.route('/one_group_prop_test', methods=['POST'])
def one_group_prop_test():
    data = request.get_json()
    solution = one_group_prop_testing(
        sample_prop = data["sample_prop"],
        sample_size = data["sample_size"],
        pop_prop = data["pop_prop"],
        pop_size = data["pop_size"],
        num_sided = data["num_sided"],
        alpha_level = data["alpha_level"],
        rand_samp = data["rand_samp"]
    )
    return {
        "solution": solution
    }


if __name__ == "__main__":
    # app.run(debug = True, host = "0.0.0.0", port = 5000)
    app.run(debug = True)