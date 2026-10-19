# SWYNEX Internship - Task 1: AI Problem Design

## Project Title: AI Student Doubt Assistant

### 1. Problem Statement
Students sometimes find it difficult to understand educational concepts and get reliable answers quickly. Searching multiple websites can be confusing and time-consuming.

The proposed AI Student Doubt Assistant will help students find answers to questions using a small collection of verified educational notes.

### 2. Target Users
- School students
- Students revising academic concepts
- Learners who need simple explanations

### 3. Proposed AI Solution
The system will accept a student's question and search a small collection of educational notes for relevant information. It will provide a short answer based on the available material.

If the information is unavailable, the system should explain that it cannot answer confidently instead of inventing an answer.

### 4. Data Source
The proposed dataset will contain 50 educational question-and-answer pairs covering basic mathematics and computer fundamentals.

Each entry will include:
- Question
- Reference answer
- Subject
- Topic

The information will be checked for accuracy before use. No personal student information will be collected.

### 5. Constraints and Limitations
- The initial version will cover only selected topics.
- Incorrect reference information could lead to incorrect answers.
- Questions outside the dataset may not receive useful answers.
- The system should not replace teachers or official educational resources.
- Student privacy must be protected.

### 6. Success Criteria
The proposed system will be evaluated using 50 test questions.

| Metric | Target |
|---|---|
| Answer correctness | At least 80% |
| Relevant responses | At least 85% |
| Unsupported answers | No more than 5% |
| Response time | Under 5 seconds |

These are proposed targets, not measured results.

### 7. Evaluation Approach
Fifty test questions will be prepared. Each response will be compared with a reference answer and reviewed for correctness, relevance, and unsupported claims.

Questions outside the dataset will also be tested to check whether the system correctly identifies its limitations.

Response times will be recorded, and the results will be used to identify areas for improvement.

### 8. Risks and Responsible AI
The assistant may provide incorrect or misleading information. To reduce this risk, it should use verified educational material and clearly indicate when it does not have enough information to answer.

Students should confirm important information with trusted educational resources.

### 9. Conclusion
The AI Student Doubt Assistant is a proposed AI solution designed to make educational information easier to access. A limited dataset, measurable success criteria, and a structured evaluation approach will help determine whether the solution is useful and reliable.
