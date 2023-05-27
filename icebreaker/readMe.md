Here we build an application called icebreaker
-This application recieves a name which then searches online for linkedin account, get information of the user from linkedin, then we generate a summarized information about that person based on the conversation about them.

We will leverage
- Chains
- Agents
- Tools
- Output Parsers
- Custom Agents

1. We will connect to linkedin to scrap data from it.
2. In the Agents/linkedin.py file we have a function to scrap linkedin data from a URL
3. Agents is used to retreive something from the outside world the LLM is not trained on.
We need the agent to look online and get us linkedin url of that user
4. We have tools/tools.py which creates a custom tool which wraps around SerpAPI which is used to perfom google searches
5. App.py file contains the chain for the prompt template, chatOpenAI
This chain is then run on the scraped linkedin data
6. We create an MVC in Flask which contains templates, static files and app.py
The app.py file contains the routes to follow to interact with frontend