import datetime

def get_text_from_notes(source):
    """
    (Placeholder) Simulates OCR or text extraction from user notes.
    """
    print(f"Reading notes from {source}...")
    # In a real project, this function would handle different file types (PDF, JPG)
    # and use a library like pytesseract or a cloud-based OCR service.
    
    # For this example, we return a sample text string.
    sample_text = """
    Artificial intelligence (AI) is intelligence—perceiving, synthesizing, and inferring information—demonstrated by machines, as opposed to intelligence displayed by animals and humans. The field of AI was founded in 1956 at a workshop at Dartmouth College. AI research is divided into subfields such as machine learning and deep learning, which are used to train AI models. The goals of AI research include reasoning, knowledge representation, planning, natural language processing, perception, and the ability to move and manipulate objects.
    """
    return sample_text

def summarize_notes(text):
    """
    (Placeholder) This function would use an NLP model to summarize a text.
    For this example, we'll return a brief, hard-coded summary.
    """
    print("Summarizing notes...")
    # In a real project, you would use an NLP library like Hugging Face Transformers.
    return "AI is intelligence demonstrated by machines, with subfields like machine learning and deep learning. Research goals include reasoning and natural language processing."

def generate_study_plan(topics_info):
    """
    Creates a personalized study plan based on topic confidence and deadlines.
    """
    print("Generating a personalized study plan...")
    today = datetime.date.today()
    
    for topic in topics_info:
        try:
            deadline = datetime.datetime.strptime(topic['deadline'], '%Y-%m-%d').date()
            days_until = (deadline - today).days
            
            confidence_weight = 11 - topic['confidence']
            deadline_weight = 1 if days_until <= 0 else 1 / days_until
            
            topic['urgency'] = confidence_weight * deadline_weight
        except (ValueError, KeyError) as e:
            print(f"Warning: Could not process topic '{topic.get('topic', '')}'. Error: {e}")
            topic['urgency'] = -1  # Assign a low urgency to sort it last
    
    valid_topics = [t for t in topics_info if 'urgency' in t and t['urgency'] != -1]
    valid_topics.sort(key=lambda x: x['urgency'], reverse=True)
    
    study_plan = {
        'high_priority': [t['topic'] for t in valid_topics if t['urgency'] > 5],
        'medium_priority': [t['topic'] for t in valid_topics if 2 < t['urgency'] <= 5],
        'low_priority': [t['topic'] for t in valid_topics if t['urgency'] <= 2]
    }
    return study_plan

# Main program to run the workflow
if __name__ == "__main__":
    print("--- Smart Study Hub: Workflow Demo ---")

    # 1. Input: Simulate a user uploading a file and providing details.
    notes_source = "User notes file"
    topics_info = [
        {'topic': 'AI Fundamentals', 'confidence': 4, 'deadline': '2025-10-25'},
        {'topic': 'Machine Learning', 'confidence': 7, 'deadline': '2025-11-10'},
        {'topic': 'Deep Learning', 'confidence': 2, 'deadline': '2025-10-05'}
    ]

    # 2. Processing: The three main steps in the workflow.
    print("\nStarting the processing pipeline...")
    
    # Step 1: Extract text from notes
    extracted_text = get_text_from_notes(notes_source)
    
    # Step 2: Summarize the extracted text
    summary = summarize_notes(extracted_text)
    
    # Step 3: Generate the study plan
    study_plan = generate_study_plan(topics_info)

    # 3. Output: Display the results to the user.
    print("\n--- Output: Your Personalized Study Plan ---")
    
    print("\nNotes Summary:")
    print(summary)
    
    print("\nYour Study Schedule:")
    for priority, topics in study_plan.items():
        print(f"\n{priority.replace('_', ' ').title()}:")
        if topics:
            for t in topics:
                print(f"- {t}")
        else:
            print("- No topics in this category.")
