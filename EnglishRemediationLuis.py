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
    st.write("Generative AI has come a long way from what was introduced back in 2014. To be more specific, the\nmost well-known chat bot, ChatGPT developed by OpenAI, has continued to improve throughout the years and")
    st.write("remains as one of the most advanced tools to exist. Besides ChatGPT, there are other impressively advanced\nchatbots like Sora, Google Gemini, Microsoft Copilot, and more.")
    st.success("Scroll through the tabs to interact, vote, simulate, and reflect!")

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

# poll: Student Opinions
elif section == "Poll: Student Opinions":
    st.header("📊 Live Poll")
    poll = st.radio("Do you personally use generative AI (like ChatGPT) for school?", 
                    ("Yes - all the time", "Sometimes", "Never"))

    st.write("Thanks for voting! Here's what others think:")
    st.bar_chart(pd.Series({
        "Yes - all the time": random.randint(10, 30),
        "Sometimes": random.randint(20, 50),
        "Never": random.randint(5, 20)
    }))

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
    st.header("📈 Survey Data: GenAI in Academia")
    #get_gdp_data()
    def get_gdp_data():
        """Grab GDP data from a CSV file.

        This uses caching to avoid having to read the file every time. If we were
        reading from an HTTP endpoint instead of a file, it's a good idea to set
        a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
        """

        # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    # DATA_FILENAME = Path(__file__).parent/'LuisStreamlit/gdp_datas.csv'
       # DATA_FILENAME = Path(__file__).parent/'data/gdp_datas.csv'
        DATA_FILENAME =r"/workspaces/gdp-dashboard/data/gdp_datas.csv"
        raw_gdp_df = pd.read_csv(DATA_FILENAME)

        MIN_YEAR = 1960
        MAX_YEAR = 2025 #2025

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
        # So let's pivot all those year-columns into two: Year and GDP
        year_cols = [str(y) for y in range(MIN_YEAR, MAX_YEAR + 1) if str(y) in raw_gdp_df.columns]
        gdp_df = raw_gdp_df.melt(
            id_vars =['Country Code'],
            value_vars = year_cols, 
            var_name = 'Year',
            value_name = 'GDP'
            #[str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
            #'Year',
            #'GDP',
        )

        # Convert years from string to integers
        #gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

        #return gdp_df
        gdp_df['Year'] = gdp_df['Year'].astype(int)
        return gdp_df

    gdp_df = get_gdp_data()

    # -----------------------------------------------------------------------------
    # Draw the actual page

    # Set the title that appears at the top of the page.
    '''
    # :earth_americas: Research on Generative AI 🤖

    Generative AI has come a long way from what was introduced back in 2014. To be more specific, the
    most well-known chat bot, ChatGPT developed by OpenAI, has continued to improve throughout the years and
    remains as one of the most advanced tools to exist. Besides ChatGPT, there are other impressively advanced
    chatbots like Sora, Google Gemini, Microsoft Copilot, and more.
    '''

    # Add some spacing
    ''
    ''

    min_value = gdp_df['Year'].min()
    max_value = gdp_df['Year'].max()

    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value +1,
        value=[min_value, max_value])

    countries = gdp_df['Country Code'].unique()

    if not len(countries):
        st.warning("Select at least one country")

    selected_countries = st.multiselect(
        'Which countries would you like to view?',
        countries,
        ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

    ''
    ''
    ''

    # Filter the data
    filtered_gdp_df = gdp_df[
        (gdp_df['Country Code'].isin(selected_countries))
        & (gdp_df['Year'] <= to_year)
        & (from_year <= gdp_df['Year'])
    ]

    st.header('AI uses over time', divider='gray')

    ''

    st.line_chart(
        filtered_gdp_df,
        x='Year',
        y='GDP',
        color='Country Code',
    )

    ''
    ''


    first_year = gdp_df[gdp_df['Year'] == from_year]
    last_year = gdp_df[gdp_df['Year'] == to_year]

    st.header(f'GDP in {to_year}', divider='gray')

    ''

    cols = st.columns(4)

    for i, country in enumerate(selected_countries):
        col = cols[i % len(cols)]

        with col:
            first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
            last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

            if math.isnan(first_gdp):
                growth = 'n/a'
                delta_color = 'off'
            else:
                growth = f'{last_gdp / first_gdp:,.2f}x'
                delta_color = 'normal'

            st.metric(
                label=f'{country} GDP',
                value=f'{last_gdp:,.0f}B',
                delta=growth,
                delta_color=delta_color
            )
    # Dummy data for student AI use frequency
    survey_data = {
        "Use AI Often": 45,
        "Use Occasionally": 30,
        "Do Not Use": 25
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

    st.info("This chart is based on a fictional survey. Replace it with real data from a class or form for more accurate results.")


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

