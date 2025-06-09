import os
from dotenv import load_dotenv
load_dotenv('/home/vans/Desktop/Ai&Ml/Linked/Linked/.env')

import google.generativeai as genai

genai.configure(api_key=os.getenv("gems"))
model = genai.GenerativeModel("gemini-1.5-flash")

##ingest the data
def summarize_readme(readmePath,techStack):

    # Read the README content
    with open(readmePath, 'r') as file:
        readme_content = file.read()

    # with open(codeBase, 'r') as file:
    #   codeBase = file.read()

    with open(techStack, 'r') as file:
        techStack = file.read()

    # Assume readme_content is defined
    # Assume techStack_explicitly_provided is defined (can be None or empty)

    # --- PROMPT 1: PROJECT ANALYSIS ---
    prompt_1_analysis = f"""
    **Act as an expert project reviewer.** Your goal is to meticulously analyze the provided project information and generate a structured summary. This summary will be used later to create other content.

    **Project Information Provided:**

    1.  **README Content:**
        ```markdown
        {readme_content}
        ```
    """


    tech_stack_info_for_prompt1 = ''
    if techStack_explicitly_provided:
        tech_stack_info_for_prompt1 = f"""
    2.  **Explicitly Provided Technology Stack:**
        ```
        {techStack_explicitly_provided}
        ```
    """
    else:
        tech_stack_info_for_prompt1 = """
    2.  **Explicitly Provided Technology Stack:** None provided. You will need to infer this.
    """

    prompt_1_analysis += tech_stack_info_for_prompt1 + f"""

    **Your Tasks:**

    1.  **Technology Stack Identification:**
        *   If an "Explicitly Provided Technology Stack" is given, use that.
        *   Otherwise, analyze the "README Content" to infer the technology stack. List identified technologies (Languages, Frameworks, Databases, Tools, etc.).
        *   Briefly note the clues from the README if inferred.

    2.  **Project Overview:**
        *   **Project Name:** Extract or infer the project name.
        *   **Elevator Pitch (1-2 sentences):** Describe its core purpose, problem solved, and unique value.

    3.  **Key Highlights & Innovations:**
        *   **Standout Features (2-3 bullet points):** Identify key features from the README.
        *   **Tech Stack Synergy:** Briefly comment on how the identified technology stack supports these features.

    4.  **Constructive Feedback & Growth Areas:**
        *   **Potential Enhancements (1-2 ideas):** Suggest future features or improvements positively.
        *   **Impact & Relevance:** Briefly discuss its potential impact or relevance.

    **Output Format:**
    Produce the output in the following structured format, using the exact headings:

    **Technology Stack Identification**
    *   [List inferred or provided technologies and any brief notes on inference]

    **Project Overview**
    *   **Project Name:** [Your finding]
    *   **Elevator Pitch (1-2 sentences):** [Your finding]

    **Key Highlights & Innovations**
    *   **Standout Features:**
        1.  [Feature 1]
        2.  [Feature 2]
        (3. [Feature 3 if applicable])
    *   **Tech Stack Synergy:** [Your comment]

    **Constructive Feedback & Growth Areas**
    *   **Potential Enhancements:**
        1.  [Enhancement 1]
        (2. [Enhancement 2 if applicable])
    *   **Impact & Relevance:** [Your comment]

    **Important Note:** Base your evaluation *solely* on the provided README content and any explicitly provided technology stack. Do not access external information or make assumptions beyond the text.
    """

    # --- (Simulate sending Prompt 1 to Gemini and getting the response) ---
    # model = ... # Your Gemini model instance
    # response_1 = model.generate_content(prompt_1_analysis)
    # structured_project_analysis = response_1.text
    # print("--- Structured Project Analysis (Output of Prompt 1) ---")
    # print(structured_project_analysis)

    # structured_project_analysis = """... (output from prompt 1 copied here) ..."""

    # --- PROMPT 2: LINKEDIN POST GENERATION ---
    prompt_2_linkedin = f"""
    **Act as a skilled social media content creator specializing in technology and project showcases.**

    You have been provided with a structured analysis of a project. Your task is to transform this analysis into an engaging and concise LinkedIn post.

    **Structured Project Analysis Provided:**

    **Your Goal:**
    Draft a LinkedIn post based *only* on the "Structured Project Analysis Provided" above.

    **LinkedIn Post Components to Generate:**
    *   **Engaging Hook (1 sentence):** Grab attention immediately.
    *   **Project Introduction (1-2 sentences):** Use the "Project Name" and "Elevator Pitch" to introduce the project and its core value.
    *   **Key Achievements/Features (2-3 concise bullet points):** Summarize the "Standout Features."
    *   **Tech Stack Mention (1 sentence, optional but encouraged):** Briefly mention key technologies from "Technology Stack Identification" and their benefit, drawing from "Tech Stack Synergy."
    *   **Enthusiastic Closing/Call to Wonder (1 sentence):** End on a positive, forward-looking note, perhaps drawing from "Impact & Relevance" or "Potential Enhancements."
    *   **Suggested Hashtags (3-5 relevant hashtags):**

    **Tone and Style for LinkedIn Post:**
    *   Enthusiastic, positive, and professional.
    *   Concise and easy to read.
    *   Highlight benefits and impact.
    *   Use emojis sparingly and appropriately if desired.

    **Output Format:**
    Provide *only* the LinkedIn post components as requested above, clearly labeled.
    """

    # --- (Simulate sending Prompt 2 to Gemini and getting the response) ---
    # response_2 = model.generate_content(prompt_2_linkedin)
    # linkedin_post_draft = response_2.text
    # print("\n--- LinkedIn Post Draft (Output of Prompt 2) ---")
    # print(linkedin_post_draft)
    response = model.generate_content(prompt_1_analysis)

    return response.text



def create_post():
  pass


# Example usage
readmePath = "/home/vans/Desktop/Sdg/OurCovid/README.md"
techStack = "/home/vans/Desktop/Sdg/OurCovid/requirements.txt"
#techStack = "/home/vans/Desktop/Sdg/OurCovid/README.md"
def techStack_explicitly_provided (techStack):
        if techStack is None or techStack.strip() == "":
            return None
        else:
            return techStack

summary = summarize_readme(readmePath,techStack)
print(summary)
