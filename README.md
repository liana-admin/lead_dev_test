# BeatsQuares Lead Developer Assessment

## Introduction

Welcome to the BeatsQuares Lead Developer Assessment. This test is designed to evaluate your skills in backend development, AI integration, media processing, and content delivery. Your performance on this assessment will be a key factor in determining your suitability for the lead developer role at BeatsQuares.

## Setup Instructions

1. Fork this repository to your personal GitHub account.
2. Clone your forked repository to your local machine.
3. Create a virtual environment
4. Install the required dependencies from requirements.txt
5. Set up a local Redis server for Celery (if not already running).
6. Run the application

   ## Tasks

### 1. Advanced Recategorization Feature

Implement a new API endpoint `/recategorize/<int:article_id>` that allows users to suggest a new category for an article. The feature should:

- Accept the article ID and the suggested new category as inputs.
- Integrate an LLM to evaluate the suggested category:
- Analyze the article content and the suggested category.
- Provide a "likeness score" indicating how well the category fits the article.
- Provide a brief explanation for its score.
- Return the likeness score and explanation to the user.
- Implement a user verification step where the user can confirm or decline the category change based on the LLM's feedback.
- If confirmed, update the article's category in the database.

### 2. Optimize Database Query

Optimize the inefficient database query in the `get_articles_by_category` function in `app/routes.py`.

### 3. Implement Robust Error Handling

Enhance the error handling for the article scraping function to gracefully handle situations where the source website is down or unresponsive.

### 4. AI-Powered Content Summarization

Implement a feature to generate a brief summary of each article using an AI service. You may use GPT-4 or an alternative service of your choice. Implement this in the `generate_summary` function in `app/routes.py`.

- Explain your choice of AI service and how you would integrate it in a production environment.
- If you choose GPT-4, also describe an alternative solution and its implementation approach.

### 5. Asynchronous Processing

Implement the `async_scrape_and_categorize` Celery task in `app/tasks.py` to perform article scraping and categorization asynchronously.

### 6. Unit Tests

Write comprehensive unit tests for the new recategorization feature and the asynchronous scraping task. Add these tests to the `tests/test_app.py` file.

### 7. API Design for Frontend

Design (but don't implement) an API endpoint that would allow a frontend application to efficiently fetch and display a paginated list of articles with their summaries. Explain your design choices in the README.

### 8. Podcast Feature Design

Design a system to automatically generate podcasts with the following requirements:
- Use existing articles with metadata: Persons, Places, Topic, Level of tragedy/humor/political relevance.
- Create a 5-minute podcast about celebrities in Hollywood, excluding highly dramatic or politically relevant topics.
- The podcast should include:
- An intro song
- Background music
- AI-generated voice narration
- Pre-recorded interviews (stored as .wav files)
- Advertisement breaks (stored as .wav files)
- An outro

Outline the key components, processes, and API endpoints needed for this feature. Describe how you would handle the audio processing and assembly of these elements.

### 9. CDN Implementation Strategy

- Identify areas in BeatsQuares' operations where a CDN could be beneficial.
- Estimate potential costs associated with CDN usage for your proposed implementation.
- Suggest alternatives to using a CDN, if any, and compare their pros and cons.
- Describe strategies for optimizing CDN usage and controlling costs.

## Submission Guidelines

1. Create a new branch in your forked repository with the naming convention: `solution-<your-name>`.
2. Implement your solutions in this branch.
3. Update this README with:
- Any additional setup instructions specific to your implementation.
- Explanations of your design choices, especially for the AI service integration and podcast feature.
- Your API design for the frontend and its rationale.
- Your podcast feature design and CDN implementation strategy.
4. Commit your changes and push the branch to your forked repository.
5. Create a pull request from your solution branch to the main branch of your forked repository.
6. Send us the link to your forked repository and the pull request.

## Evaluation Criteria

Your submission will be evaluated based on:

1. **Technical Implementation:**
- Quality and efficiency of code, especially for new features and optimizations.
- Effectiveness of AI integration for categorization and summarization.
- Implementation of asynchronous processing.
- Quality and coverage of unit tests.

2. **Problem-Solving and Feature Design:**
- Innovative and practical approach to podcast generation.
- Comprehensive understanding of CDN implementation and alternatives.

3. **Code Quality and Documentation:**
- Clean, readable, and well-structured code.
- Clear and comprehensive documentation.

4. **Scalability and Performance Considerations:**
- Strategies for scaling the application, especially for podcast generation and content delivery.
- Effective approaches to CDN cost control and performance optimization.

5. **AI Integration and Understanding:**
- Effective use of AI services with clear justification of choices.
- Understanding of alternative AI solutions and their trade-offs.

6. **Media Processing Knowledge:**
- Demonstrated understanding of audio processing and podcast production workflows.

Good luck! We look forward to reviewing your solution.
