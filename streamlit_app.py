import streamlit as st
import pandas as pd
import random
import pandas as pd
import math
from pathlib import Path

# page config
st.set_page_config(page_title="GenAI vs. The Student Mind", layout="centered")


# custom title
st.title("🤖 GenAI vs. The Student Mind")
st.subheader("Exploring the Impact of Generative AI on College Students")

# sidebar navigation
section = st.sidebar.radio("Navigate", [
    "Welcome", "Research Questions", "Poll: Student Opinions", 
    "Case Studies", "Pros vs. Cons", "AI Simulator", "Data Visualization", "Conclusion"
])

# welcome Page
if section == "Welcome":
    st.markdown("### 📈 The Rise of Generative AI")
    st.image("https://www.pega.com/sites/default/files/styles/1024/public/media/images/2023-11/pega-generative-ai-explainer-intro-img.png?itok=8AQr11PC", caption="AI in Education", use_container_width=True)
    st.write("Generative AI has come a long way from what was introduced back in 2018. To be more specific, the\nmost well-known chat bot, ChatGPT developed by OpenAI, has continued to improve throughout the years and")
    st.write("remains as one of the most advanced tools to exist. Besides ChatGPT, there are other impressively advanced\nchatbots like Sora, Google Gemini, Microsoft Copilot, and more.")
    st.success("Click through the tabs to interact, vote, simulate, and reflect!")

# research Questions
elif section == "Research Questions":
    st.header("❓ Research Questions")
    questions = [
        "How is generative AI currently used by college students?",
        "Does GenAI enhance or diminish critical thinking?",
        "Should AI tools like ChatGPT be banned or embraced in schools?",
        "What ethical concerns arise from student-AI interaction?"
    ]
    for q in questions:
        st.markdown(f"- {q}")

# Dummy data for student AI use frequency
elif section == "Poll: Student Opinions":
    survey_data = {
        "Use AI Often": 27,
        "Use Occasionally": 58,
        "Do Not Use": 13
    }

    # Convert to DataFrame
    survey_df = pd.DataFrame.from_dict(survey_data, orient='index', columns=["% of Students"])
    survey_df.index.name = "Response"

    # Chart of survey results
    st.subheader("🗳️ How often do students use Generative AI tools (e.g., ChatGPT)?")
    st.bar_chart(survey_df)

    # Interpretation
    st.markdown("""
    - 🟢 **Use AI Often** – Students frequently rely on GenAI for writing, brainstorming, or studying.
    - 🟡 **Use Occasionally** – These students use GenAI sparingly or for support roles only.
    - 🔴 **Do Not Use** – Either unaware of the tools, prefer traditional methods, or fear ethical issues.
    """)

    st.info("This chart is based on a survey where random students in Ball State University were asked to answer a single question. This survey was completely anonymous.")

# case Studies
elif section == "Case Studies":
    st.header("🧠 Case Study Scenarios")
    cases = {
        "A student writes their entire essay using ChatGPT.": "The professor noticed and gave a zero for plagiarism.",
        "A student brainstorms essay ideas with ChatGPT.": "They wrote the essay themselves and received high marks for creativity.",
        "A professor bans AI but students use it secretly.": "Grades improved, but critical thinking declined."
    }

    for scenario, outcome in cases.items():
        if st.button(scenario):
            st.info(f"📘 Outcome: {outcome}")

# Pros vs. Cons
elif section == "Pros vs. Cons":
    st.header("⚖️ Should GenAI be in the Classroom?")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Pros")
        st.markdown("""
        - Enhances creativity and brainstorming  
        - Boosts productivity  
        - Aids in accessibility  
        - Personalized learning
        """)

    with col2:
        st.subheader("⚠️ Cons")
        st.markdown("""
        - Encourages plagiarism  
        - Reduces critical thinking  
        - Blurs authorship integrity  
        - May worsen academic inequality
        """)

# AI Simulator
elif section == "AI Simulator":
    st.header("🤖 Try the AI Simulator")
    prompt = st.text_input("Enter a simple essay prompt (e.g., 'Climate Change')")
    if prompt:
        st.markdown("### ✍️ Simulated AI Response:")
        st.write(f"**Prompt:** {prompt}")
        st.write(f"**Response:** Generative AI can write full essays on '{prompt}', but relying solely on AI may hinder your ability to critically evaluate information.")
        st.warning("Would this be ethical in your class?")



# data visualization
#modification here'
elif section == "Data Visualization":
    #get_gdp_data()
    @st.cache_data
    def get_gdp_data():
        """Grab GDP data from a CSV file.

        This uses caching to avoid having to read the file every time. If we were
        reading from an HTTP endpoint instead of a file, it's a good idea to set
        a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
        """

        # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
        DATA_FILENAME = Path(__file__).parent/'data/AI_uses.csv'
        raw_gdp_df = pd.read_csv(DATA_FILENAME)

        MIN_YEAR = 2018
        MAX_YEAR = 2025

        # The data above has columns like:
        # - Country Name
        # - Country Code
        # - [Stuff I don't care about]
        # - GDP for 1960
        # - GDP for 1961
        # - GDP for 1962
        # - ...
        # - GDP for 2022
        #
        # ...but I want this instead:
        # - Country Name
        # - Country Code
        # - Year
        # - GDP
        #
        # So let's pivot all those year-columns into two: Year and Usage
        year_cols = [str(y) for y in range(MIN_YEAR, MAX_YEAR + 1) if str(y) in raw_gdp_df.columns]
        gdp_df = raw_gdp_df.melt(
            #id_vars =['Country Code'],
            id_vars =['AI Name','AI Code'],
            value_vars = year_cols, 
            var_name = 'Year',
            value_name = 'Usage (%)' #update
            #[str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
            #'Year',
            #'GDP',
        )

        # Convert years from string to integers
        #gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

        #return gdp_df
        gdp_df['Year'] = gdp_df['Year'].astype(int)
     
        
   

        return gdp_df

    gdp_df= get_gdp_data()

    # -----------------------------------------------------------------------------
  
        
    #-----------------------------------------------------------------------------
    # Draw the actual page

    # Set the title that appears at the top of the page.
    '''
    # :earth_americas: Research on Generative AI 🤖

    This chart demonstrates how the use of the now popular AI's has skyrocketed in just a couple of years.
    All data shown here has been collected using Google Trends' time frame.

    '''

    # Add some spacing
    ''
    ''


    min_value = gdp_df['Year'].min()
    max_value = gdp_df['Year'].max()
    
#value=[min_value, max_value]),
    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        #Original code
        #max_value=max_value +1,
        max_value=max_value,    #remove +1
        value=(min_value, max_value),   
        step = 1     #add in step
        )
    countries = gdp_df['AI Code'].unique()

    if not len(countries):
        st.warning("Select at least one country")

    selected_countries = st.multiselect(
        'Which AI would you like to view?',
        countries,
        ['GPT', 'SRA', 'GGI', 'MCP'])

    ''
    ''
    ''
    
    # Filter and plot
    # Filter the data
    filtered_gdp_df = gdp_df[
        (gdp_df['AI Code'].isin(selected_countries))
        & (gdp_df['Year'] <= to_year)
        & (from_year <= gdp_df['Year'])
    ]

    st.header('AI uses over time', divider='gray')

    ''

    st.line_chart(
        filtered_gdp_df,
        x='Year',
        y='Usage (%)', #Modify this
        color='AI Code',
    )

    ''
    ''
    
    
    first_year = gdp_df[gdp_df['Year'] == from_year]
    last_year = gdp_df[gdp_df['Year'] == to_year]
    

# conclusion
elif section == "Conclusion":
    st.header("📚 Wrapping It Up")
    st.markdown("""
    Generative AI isn’t going anywhere. Whether it’s a tool or a threat depends on **how** we use it.

    - Encourage ethical AI use
    - Redesign assignments for creativity
    - Teach students to use AI responsibly

    🧠 The future of education is collaborative – with both humans and machines!
    """)
    st.balloons()

