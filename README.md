# SynthFlow🍃

A tool for generating synthetic data.

# Pipelines

- Basic

|No|Pipeline|none|txt|pdf|Comment|
|---|---|---|---|---|---|
|01|Simple Q&A|❌|[✅](pipelines/Basic.py#L4)|❌|*Based on what type of document?*|

- For Learning

|No|Pipeline|none|txt|pdf|Comment|
|---|---|---|---|---|---|
|01|[Definitions and Terminology](docs/mainframe_learning_instruction_data.md#1-definitions-and-terminology)|❌|[✅](pipelines/Learning.py#L572)|❌||
|02|[Troubleshooting](docs/mainframe_learning_instruction_data.md#2-troubleshooting)|❌|[✅](pipelines/Learning.py#L513)|❌||
|03|[Command References](docs/mainframe_learning_instruction_data.md#3-command-references)|❌|[✅](pipelines/Learning.py#L454)|❌||
|04|[System Operations](docs/mainframe_learning_instruction_data.md#4-system-operations)|❌|[✅](pipelines/Learning.py#L395)|❌||
|05|[Programming on Mainframes](docs/mainframe_learning_instruction_data.md#5-programming-on-mainframes)|❌|[✅](pipelines/Learning.py#L336)|❌||
|06|[System Configuration](docs/mainframe_learning_instruction_data.md#6-system-configuration)|❌|[✅](pipelines/Learning.py#L276)|❌||
|07|[Migration and Modernization](docs/mainframe_learning_instruction_data.md#7-migration-and-modernization)|❌|[✅](pipelines/Learning.py#L217)|❌||
|08|[Performance Optimization](docs/mainframe_learning_instruction_data.md#8-performance-optimization)|❌|[✅](pipelines/Learning.py#L158)|❌||
|09|[Integration](docs/mainframe_learning_instruction_data.md#9-integration)|❌|[✅](pipelines/Learning.py#L99)|❌||
|10|[Error Analysis](docs/mainframe_learning_instruction_data.md#10-error-analysis)|❌|[✅](pipelines/Learning.py#L40)|❌||

- For Coding

|No|Pipeline|none|txt|pdf|Comment|
|---|---|---|---|---|---|
|01|[SQL Query Assistance](docs/coding_instruction_data.md#10-sql-query-assistance)|[✅](pipelines/Coding.py#L40)|❌|❌|*Requirement*|
|02|[Code Generation](docs/coding_instruction_data.md#3-code-generation)|[✅](pipelines/Coding.py#L570)|❌|❌|*Requirement*|
|03|[Code Completion](docs/coding_instruction_data.md#4-code-completion)|[✅](pipelines/Coding.py#L486)|❌|❌|*Requirements + Incomplete Code*|
|04|[Code Debugging](docs/coding_instruction_data.md#2-code-debugging)|[✅](pipelines/Coding.py#L626)|❌|❌|*Requirements + Buggy Code*|
|07|[Error Explanation](docs/coding_instruction_data.md#8-error-explanation)|[✅](pipelines/Coding.py#L181)|❌|❌|*Requirements + Buggy Code + Error Message*|
|05|[Code Explanation](docs/coding_instruction_data.md#1-code-explanation)|[✅](pipelines/Coding.py#L685)|❌|❌|*Requirements + Completed Code*|
|06|[Code Review](docs/coding_instruction_data.md#7-code-review)|[✅](pipelines/Coding.py#L243)|❌|❌|*Requirements + Completed Code*|
|08|[Code Documentation](docs/coding_instruction_data.md#9-code-documentation)|[✅](pipelines/Coding.py#L97)|❌|❌|*Requirements + Completed Code*|
|09|[Code Optimization](docs/coding_instruction_data.md#6-optimization-suggestions)|[✅](pipelines/Coding.py#L329)|❌|❌|*Requirements+Completed Code*|
|10|[Code Translation](docs/coding_instruction_data.md#5-code-translation)|[✅](pipelines/Coding.py#L410)|❌|❌|*Requirements + Completed Code*|


- Other

# TODOs
| No | Task                                         | Status |
|----|----------------------------------------------|--------|
| 01 | Improve data quality (self-instruct, evol-instruct, validator, eliminator,...)  | 🛠️     |
| 02 | Support multi-threaded running               | ❌     |
| 03 | Generate a synthetic dataset for training the model | ❌ |

# References

[gitingest](https://github.com/cyclotruc/gitingest)

[h2o-wizardlm](https://github.com/h2oai/h2o-wizardlm?tab=readme-ov-file)

[self-instruct](https://github.com/yizhongw/self-instruct)

[openai](https://platform.openai.com/docs/overview)

[openai-python](https://github.com/locchh/openai-python)

[docling](https://github.com/DS4SD/docling)

[docling.io](https://ds4sd.github.io/docling/#ibm-open-source-ai)

[WizardLM: Empowering Large Language Models to Follow Complex Instructions](https://arxiv.org/abs/2304.12244)

[Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560)