import argparse
from model.model_prediction import ModelPred

def main(user_id):
    model_pred = ModelPred()
    model_pred.predict(user_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prediction with arguments")
    parser.add_argument("--user_id", type=int, help="User Id")

    args = parser.parse_args()

    main(args.user_id)