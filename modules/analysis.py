def analyze_score(score):
    if score >= 20:
        return "Low Risk","Normal Cognitive Response"
    elif 10 <= score < 20:
        return "Moderate Risk","Mild Cognitive Impairment Suspected"
    else:
        return "High Risk","Further Clinical Evaluation Recommended"