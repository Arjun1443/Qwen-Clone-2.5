# Qwen2.5 GRPO Fine-Tuning Study

A notebook exploring GRPO fine-tuning of `Qwen/Qwen2.5-3B-Instruct` using Unsloth and the GSM8K dataset.

## Why this project matters

Reward-based fine-tuning illustrates the interaction between training data, reward functions, model updates, and generated answers.

## Technical focus

Python · Unsloth · TRL · GRPO · Hugging Face datasets · vLLM

## Explore the implementation

Open [the notebook](<Qwen2_5_(3B)_GRPO.ipynb>) to inspect preprocessing, implementation, and saved outputs.

## Run locally

```bash
git clone https://github.com/Arjun1443/Qwen-Clone-2.5.git
cd Qwen-Clone-2.5
python -m venv .venv
# Activate .venv before continuing.
python -m pip install jupyter jupyter
python -m jupyter notebook
```

Select `Qwen2_5_(3B)_GRPO.ipynb` in Jupyter and review its configuration before executing cells in order.

## Reproducibility notes

The notebook includes Unsloth branding and setup material; original authors retain credit. Run in a compatible CUDA/GPU environment and follow the notebook's installation cells rather than assuming a CPU setup will work. Review downloads, hardware requirements, model terms, and reward functions before training. The repository name does not imply that Qwen was built from scratch.

Saved notebook outputs describe a prior execution; they are not an independently reproduced benchmark. Dependency versions are not locked, so compatibility may require adjustment.


## Author

[Naga Anweesh Reddy](https://github.com/Arjun1443/Naga-Anweesh-Reddy) · AI development and technical training
