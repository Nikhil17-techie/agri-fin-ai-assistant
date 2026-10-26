# AI Smart Agriculture & Finance Assistant

## Prompt Engineering Experiment Results

### 1. Experiment Objective

The objective of this experiment is to compare three prompt engineering techniques: Zero-Shot Prompting, Role-Based Prompting, and Structured Prompting.

The experiment examines how different prompt designs influence the relevance, clarity, organization, and practical usefulness of AI-generated agricultural guidance.

### 2. Experiment Setup

* **Project Name:** AI Smart Agriculture & Finance Assistant
* **AI Model:** Gemini 3.8 Flash, as configured in the experiment script
* **Programming Language:** Python
* **API:** Google Gemini API
* **Experiment Domain:** Agriculture
* **Number of Techniques Tested:** 3

### 3. Common Test Question

The same question was used for all three experiments:

> My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?

Using the same question helps maintain consistency when comparing the responses.

### 4. Experiment 1: Zero-Shot Prompting

#### Prompt Technique

Zero-shot prompting provides the AI model with a direct question without assigning a specific role or requiring a predefined response structure.

#### Prompt Used

My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?

#### Actual Result

The model identified several possible causes of yellow leaves and slow growth in tomato plants.

Its response discussed:

* Overwatering and poor drainage.
* Nitrogen deficiency.
* Cold temperatures and insufficient sunlight.
* Root-bound plants.
* Soil pH imbalance.

The model recommended checking soil moisture, observing which leaves were yellowing, examining temperatures, and considering the plant's growing conditions before applying treatments.

#### Observation

The response contained detailed explanations and practical recommendations even though the prompt was relatively simple. However, it was not restricted to a specific output format and included several sections chosen by the model.

### 5. Experiment 2: Role-Based Prompting

#### Prompt Technique

Role-based prompting assigns the AI model a domain-specific role to encourage relevant explanations and practical guidance.

#### Prompt Used

Act as an agricultural extension assistant who provides practical guidance to farmers.

Question: My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?

Explain possible reasons for the problem and suggest practical first steps. Use simple language.

#### Actual Result

The model responded in a farmer-friendly, advisory style.

It discussed:

* Overwatering.
* Nutrient deficiencies, particularly nitrogen deficiency.
* Underwatering.
* Pests and soil diseases.

It recommended checking soil moisture, observing where the yellowing occurred, inspecting the undersides of leaves, and selecting appropriate actions based on the observations.

The response also invited the user to provide additional information to help narrow down the possible cause.

#### Observation

Compared with the zero-shot response, the role-based response presented its recommendations as a practical check-up followed by possible causes and solutions. The assigned role encouraged a more conversational and advisory style.

### 6. Experiment 3: Structured Prompting

#### Prompt Technique

Structured prompting combines a role, explicit instructions, precautions, and a predefined output format.

The objective is to make the answer organized and easier to follow.

#### Prompt Used

You are an agricultural guidance assistant.

Task: Help the user understand the tomato plant problem and identify appropriate first steps.

Question: My tomato plants have yellow leaves and slow growth. What could be the reasons, and what should I do first?

Instructions:

1. Explain possible causes without claiming a definite diagnosis.
2. Recommend simple checks the user can perform first.
3. Give practical next steps based on the observations.
4. Include relevant precautions.
5. Do not recommend unnecessary chemicals or excessive fertilizer.

Use the following output format:

* Possible Causes
* First Steps
* Precautions
* Follow-up Questions

#### Actual Result

The model followed the requested structure and organized its response into four sections.

**Possible Causes:**

* Watering imbalances.
* Nutrient deficiencies.
* Inadequate sunlight or low temperatures.
* Poor drainage or root compaction.
* Pests or root problems.

**First Steps:**

* Check soil moisture.
* Observe the pattern of yellowing.
* Inspect leaves for pests.
* Evaluate sunlight exposure.

**Precautions:**

* Avoid applying excessive fertilizer before understanding the problem.
* Avoid chemical treatments before identifying a likely pest or disease.
* Water the soil at the base of the plant rather than unnecessarily wetting the leaves.

**Follow-up Questions:**

The model asked about the location of the yellow leaves, the growing environment, watering frequency, and soil drainage.

#### Observation

The structured response followed the requested headings and included precautions and follow-up questions. This made its organization predictable and helped separate possible causes from recommended actions.

### 7. Comparative Evaluation

The following table summarizes the observed characteristics of the three actual responses.

| Evaluation Criterion      | Zero-Shot Prompting                           | Role-Based Prompting                                | Structured Prompting                            |
| ------------------------- | --------------------------------------------- | --------------------------------------------------- | ----------------------------------------------- |
| Relevance                 | Relevant to the question                      | Relevant to the question                            | Relevant to the question                        |
| Clarity                   | Detailed explanation                          | Conversational guidance                             | Clearly separated sections                      |
| Organization              | Multiple sections chosen by the model         | Check-up, causes, and practical fixes               | Followed the requested headings                 |
| Practical recommendations | Soil, temperature, sunlight, and other checks | Soil, leaf patterns, pests, and conditional actions | Soil, leaf patterns, pests, and sunlight checks |
| Precautions               | Included some treatment cautions              | Included practical cautions                         | Explicitly included a precautions section       |
| Follow-up questions       | Not a dedicated section                       | Asked the user to report observations               | Included specific follow-up questions           |

**Evaluation approach:** This is a qualitative comparison based on the generated responses. It is not a scientific measurement of accuracy or overall performance.

### 8. Key Findings

The experiment produced the following observations:

1. **Zero-Shot Prompting:** A direct question was sufficient to generate a relevant and detailed response.
2. **Role-Based Prompting:** Assigning an agricultural-assistant role encouraged a conversational, farmer-oriented response.
3. **Structured Prompting:** Explicit instructions and predefined headings produced a response that followed the requested organization.
4. **Similarities:** All three responses discussed watering problems, nutrient deficiencies, and the importance of examining plant conditions.
5. **Differences:** The responses differed in their organization, explanations, recommendations, and use of follow-up questions.

The main observed difference was not that the three techniques produced entirely different answers, but that they presented similar agricultural guidance in different ways.

### 9. Conclusion

The experiment successfully compared Zero-Shot Prompting, Role-Based Prompting, and Structured Prompting using the same agricultural question.

Zero-shot prompting demonstrated that a simple question can generate relevant guidance. Role-based prompting encouraged a more conversational and domain-oriented response. Structured prompting provided greater control over the organization and presentation of the answer.

For this experiment, structured prompting was particularly useful when predictable sections, explicit precautions, and follow-up questions were desired.

However, this conclusion is limited to the tested question and generated responses. Additional experiments would be required to determine whether the same patterns hold across different agricultural problems and domains.

### 10. Limitations

* The experiment used one primary agricultural question.
* The responses were evaluated qualitatively rather than using a standardized scoring system.
* AI responses may vary across repeated runs.
* Temporary API errors may affect execution, although retry handling allowed all three experiments to complete successfully in this run.
* The experiment did not independently verify every agricultural recommendation.
* Real agricultural problems may require local conditions, crop growth stage, soil information, and expert assessment.

### 11. Responsible Use

The assistant provides general agricultural information and should not be treated as a substitute for qualified agricultural advice.

Users should verify recommendations against their actual growing conditions. Fertilizers and crop-protection products should be used appropriately and according to product labels and relevant local guidance.

The assistant should communicate uncertainty when the available information is insufficient to identify the cause of a plant problem confidently.

### 12. Project Files

| File                 | Purpose                                                             |
| -------------------- | ------------------------------------------------------------------- |
| `app.py`             | Implements the Streamlit application                                |
| `test_prompts.py`    | Runs the three prompt engineering experiments                       |
| `prompt_outputs.txt` | Stores the experiment prompts and generated responses               |
| `prompt_results.md`  | Documents the experiment setup, results, comparison, and conclusion |

---

**End of Experiment Report**
