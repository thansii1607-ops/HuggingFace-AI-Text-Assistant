import streamlit as st
from transformers import pipeline

# Page Configuration
st.set_page_config(
    page_title="Hugging Face AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Application Title
st.title("🤖 Hugging Face AI Text Assistant")
st.write(
    "Perform text summarization, translation, "
    "sentiment analysis, and question answering."
)

st.divider()


# Load AI Models
@st.cache_resource
def load_models():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

    translator = pipeline(
        "translation_en_to_fr",
        model="Helsinki-NLP/opus-mt-en-fr"
    )

    sentiment = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    question_answerer = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad"
    )

    return summarizer, translator, sentiment, question_answerer


# Initialize Models
try:
    with st.spinner("Loading AI models... Please wait."):
        summarizer, translator, sentiment, question_answerer = load_models()

    st.success("✅ AI models loaded successfully!")

except Exception as e:
    st.error("❌ Unable to load AI models.")
    st.error(str(e))
    st.info(
        "Check your internet connection and installed packages. "
        "AI models must download successfully before use."
    )
    st.stop()


# Create Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Summarization",
    "🌐 Translation",
    "😊 Sentiment Analysis",
    "❓ Question Answering"
])


# 1. TEXT SUMMARIZATION
with tab1:
    st.header("📝 Text Summarization")

    text = st.text_area(
        "Enter a paragraph to summarize:",
        height=200,
        key="summary_text"
    )

    if st.button("Summarize Text"):
        if not text.strip():
            st.warning("Please enter some text.")

        elif len(text.split()) < 30:
            st.warning("Please enter at least 30 words.")

        else:
            with st.spinner("Summarizing text..."):
                try:
                    result = summarizer(
                        text,
                        max_length=100,
                        min_length=20,
                        do_sample=False,
                        truncation=True
                    )

                    st.subheader("Summary")
                    st.success(result[0]["summary_text"])

                except Exception as e:
                    st.error(f"Summarization failed: {e}")


# 2. ENGLISH TO FRENCH TRANSLATION
with tab2:
    st.header("🌐 English to French Translation")

    text = st.text_area(
        "Enter English text:",
        height=150,
        key="translation_text"
    )

    if st.button("Translate Text"):
        if not text.strip():
            st.warning("Please enter English text.")

        else:
            with st.spinner("Translating text..."):
                try:
                    result = translator(
                        text,
                        max_length=200,
                        truncation=True
                    )

                    st.subheader("Translated Text")
                    st.success(result[0]["translation_text"])

                except Exception as e:
                    st.error(f"Translation failed: {e}")


# 3. SENTIMENT ANALYSIS
with tab3:
    st.header("😊 Sentiment Analysis")

    text = st.text_area(
        "Enter a sentence or review:",
        height=120,
        key="sentiment_text"
    )

    if st.button("Analyze Sentiment"):
        if not text.strip():
            st.warning("Please enter a sentence.")

        else:
            with st.spinner("Analyzing sentiment..."):
                try:
                    result = sentiment(text[:1000])[0]

                    label = result["label"]
                    score = result["score"]

                    st.subheader("Analysis Result")

                    if label == "POSITIVE":
                        st.success("😊 Sentiment: Positive")
                    else:
                        st.error("😞 Sentiment: Negative")

                    st.write(
                        f"Confidence: {score * 100:.2f}%"
                    )

                    st.progress(float(score))

                except Exception as e:
                    st.error(f"Sentiment analysis failed: {e}")


# 4. QUESTION ANSWERING
with tab4:
    st.header("❓ Question Answering")

    context = st.text_area(
        "Enter the paragraph:",
        height=200,
        key="qa_context"
    )

    question = st.text_input(
        "Enter your question:"
    )

    if st.button("Get Answer"):
        if not context.strip() or not question.strip():
            st.warning(
                "Please enter both the paragraph and the question."
            )

        else:
            with st.spinner("Finding the answer..."):
                try:
                    result = question_answerer(
                        question=question,
                        context=context[:5000]
                    )

                    st.subheader("Answer")
                    st.success(result["answer"])

                    st.write(
                        f"Confidence: {result['score'] * 100:.2f}%"
                    )

                except Exception as e:
                    st.error(f"Question answering failed: {e}")


# Footer
st.divider()
st.caption(
    "Built using Python, Streamlit, and Hugging Face Transformers."
)