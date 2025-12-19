# Evaluation Protocol

To ensure a fair and standardized evaluation protocol, we release the full **FysicsWorld** dataset with ground-truth answers withheld.  
In addition, we provide a **test-mini** subset (300 samples) that includes ground-truth answers for local validation and debugging purposes.

## Submission Format

- For each task, please submit a **separate JSON file** containing your model predictions.
- Each JSON file should follow the task-specific submission format described in this repository.

### Multimedia Outputs

If the model output includes **multimedia content** (e.g., images, videos, audio, or other binary artifacts):

- Please include the corresponding multimedia files in your submission package.
- Specify the **relative file path** to each multimedia output in the `predictions` field of the JSON file.

## Evaluation and Leaderboard

We will update the **Leaderboard** as soon as we receive your model results.

Due to the diversity of tasks and the complexity of multimodal outputs, the current automated evaluation suite is still under active development.  
We will continue to improve and expand the evaluation pipeline to better support different modalities and task types.

## Maintenance Commitment

We are committed to the long-term maintenance of the **FysicsWorld** dataset and evaluation framework.  
Specifically, we will:
- Continuously curate and improve data quality,
- Actively maintain and update the data repository,
- Iteratively refine and optimize the evaluation suite and methodologies.

We welcome feedback and contributions from the community to help improve the benchmark.