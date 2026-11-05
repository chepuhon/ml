NUM_OF_STEPS = 3

REPORT_TEMPLATE = (
    "Report\n\n"
    "We have made {total} observations from tossing a coin: "
    "{tails} of them were tails and {heads} of them were heads. "
    "The probabilities are {tail_percent:.2f}% and {head_percent:.2f}%, respectively. "
    "Our forecast is that in the next {steps} observations we will have: "
    "{pred_tails} tail and {pred_heads} heads."
)
