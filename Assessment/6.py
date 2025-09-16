# 6. Customer Feedback Analysis
def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"

    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)

if __name__ == "__main__":
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    print("Positive Feedback:", str(positive_feedback_percentage(ratings)) + "%")