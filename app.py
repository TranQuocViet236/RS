from flask import Flask, request
from model.model_prediction import ModelPred

app = Flask(__name__)


@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    # get user_id
    user_id = request.args.get('user_id')
    print(type(user_id))

    # prediction with user_id
    if user_id is not None:
        model_pred = ModelPred()
        result_df = model_pred.predict(int(user_id))

        # Return Dataframe as JSON
        return result_df.to_json(orient='records')

    # If invalid user_id
    return 'Missing user_id parameter', 400


if __name__ == '__main__':
    app.run(debug=True)