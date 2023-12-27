# Lang-bot

## An assistant generative AI agent

Provides HR employees with guidance, precedents, and training for their day-to-day roles. The assistant will answer
questions related to its own training, onboarding, candidates faqs or procedural documentation.

### Requirements
- Python 3 
- Dependecies in ```poetry.lock``` file
- Hugging Face / Open AI accounts, configure environment variables ```HUGGINGFACEHUB_API_TOKEN```/```OPENAI_API_KEY``` 

### Installation

#### Using Poetry
```bash
poetry install
```
NOTE: Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. In no case, it should be installed in the environment of the project that is to be managed by Poetry.

#### Or using pip 
```bash
$> pip install -r requirements.txt
```

### Execution 
```bash
python3 ./main.py
```

### Example conversation 
```
Chatbot: Hi! I'm your Virtual Assistant. I can answer questions about HR Inc., what do you wanna know?
Chatbot: You can write 'bye' to end the conversation

You: What's the procedure for onboarding new employees?
Chatbot:  The procedure for onboarding new employees at the Human Resources department involves several steps, including obtaining necessary documentation, coordinating with IT for setup, preparing a welcome kit, conducting a welcome meeting, providing an HR orientation, scheduling training sessions, communicating performance expectations, establishing a feedback loop, introducing a mentor, facilitating social integration, and continuously supporting and integrating the new employee into the organization. This comprehensive onboarding process aims to provide a positive experience for new hires, ensuring their smooth integration into the organization.

You: Is there any candidate specialized in AI? 
Chatbot:  The candidate  Eugenia Piñeiro, has a strong background in artificial intelligence and has developed strategies that have contributed to the field of medicine. 

You: What does hr inc do? 
Chatbot:  HR Inc. Is a premier HR solutions provider that offers tailored HR solutions, recruitment expertise, employee development programs, compliance and risk management services, and HR technology solutions to help organizations build thriving workplaces and achieve their full potential. They also promote diversity, equity, and inclusion, effective communication, employee engagement, and conflict resolution. Their virtual assistant, HRBot, integrates with existing HR systems and applications to enhance collaboration, data accuracy, and overall workflow efficiency.

You: bye
Chatbot:  Goodbye! If you have any further questions, please don't hesitate to reach out. Have a great day!
```