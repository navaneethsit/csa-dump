import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# --------------------
# Load Questions
# --------------------
from questions.questions import questions as questions_set1
from questions.question2 import questions as questions_set2

# --------------------
# Streamlit Setup
# --------------------
st.set_page_config(
    page_title="CSA Practice Quiz Pro | Enterprise Learning Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Professional CSS
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Professional Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Professional Cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .metric-card h3 {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .metric-card p {
        color: #7f8c8d;
        margin: 0.25rem 0;
        font-size: 0.9rem;
    }
    
    /* Progress Container */
    .progress-container {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    .progress-bar {
        background: #e0e0e0;
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
    }
    
    /* Question Cards */
    .question-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 1.5rem 0;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .question-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .question-card h3 {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1rem;
        line-height: 1.4;
    }
    
    /* Professional Timer */
    .timer {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-align: center;
        font-weight: 600;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(255, 107, 107, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
        font-size: 1.1rem;
    }
    
    /* Enhanced Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:disabled {
        background: #bdc3c7;
        transform: none;
        box-shadow: none;
        cursor: not-allowed;
    }
    
    /* Secondary Button Style */
    .secondary-button {
        background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%) !important;
    }
    
    /* Success/Error States */
    .success-card {
        border-left: 5px solid #00d4aa !important;
        background: linear-gradient(135deg, #f8fff9 0%, #e8f5e8 100%);
    }
    
    .error-card {
        border-left: 5px solid #ff595e !important;
        background: linear-gradient(135deg, #fff8f8 0%, #ffe8e8 100%);
    }
    
    /* Results Dashboard */
    .results-header {
        background: linear-gradient(135deg, #00d4aa 0%, #00b894 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 212, 170, 0.3);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    /* Typography Improvements */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 600;
    }
    
    /* Custom Metrics */
    .custom-metric {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    .custom-metric h4 {
        color: #7f8c8d;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .custom-metric h2 {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Navigation Buttons */
    .nav-buttons {
        display: flex;
        gap: 1rem;
        margin: 2rem 0;
        justify-content: center;
    }
    
    /* Filter Section */
    .filter-section {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    /* Performance Chart Container */
    .chart-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .metric-card {
            padding: 1rem;
        }
        
        .question-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --------------------
# Initialize session state
# --------------------
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'selected_questions' not in st.session_state:
    st.session_state.selected_questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'question_set' not in st.session_state:
    st.session_state.question_set = None
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'quiz_time_limit' not in st.session_state:
    st.session_state.quiz_time_limit = 60
if 'performance_history' not in st.session_state:
    st.session_state.performance_history = []

# --------------------
# Professional Sidebar
# --------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: white; margin-bottom: 0.5rem;">🎓 CSA Quiz Pro</h2>
        <p style="color: #bdc3c7; font-size: 0.9rem;">Professional Learning Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## ⚙️ Configuration")
    
    # Quiz settings
    with st.expander("📋 Quiz Settings", expanded=True):
        time_limit = st.slider("⏱️ Time Limit (minutes)", 15, 120, 60, 15)
        st.session_state.quiz_time_limit = time_limit
        
        questions_per_quiz = st.slider("📝 Questions per Quiz", 10, 100, 30, 5)
        
        study_mode = st.checkbox("📖 Study Mode", help="Show explanations immediately after answering")
    
    st.markdown("---")
    
    # Performance stats
    st.markdown("## 📊 Performance Analytics")
    
    if st.session_state.performance_history:
        avg_score = sum([h['score'] for h in st.session_state.performance_history]) / len(st.session_state.performance_history)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📈 Avg Score", f"{avg_score:.1f}%")
        with col2:
            st.metric("📚 Quizzes", len(st.session_state.performance_history))
        
        # Best performance
        best_score = max([h['score'] for h in st.session_state.performance_history])
        st.metric("🏆 Best Score", f"{best_score:.1f}%")
        
        # Recent trend
        if len(st.session_state.performance_history) >= 3:
            recent_avg = sum([h['score'] for h in st.session_state.performance_history[-3:]]) / 3
            trend = "↗️" if recent_avg > avg_score else "↘️" if recent_avg < avg_score else "➡️"
            st.metric("📊 Recent Trend", f"{recent_avg:.1f}%", trend)
    else:
        st.info("🎯 Take your first quiz to unlock analytics!")

# --------------------
# Professional Header
# --------------------
st.markdown("""
<div class="main-header">
    <h1>🎓 CSA Practice Quiz Pro</h1>
    <p>Master ServiceNow Certified System Administrator concepts with our professional learning platform</p>
</div>
""", unsafe_allow_html=True)

# --------------------
# Question Set Selection
# --------------------
if not st.session_state.quiz_started:
    st.markdown("### 🎯 Select Your Learning Path")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📖 Foundation Set</h3>
            <p><strong>Questions:</strong> 309</p>
            <p><strong>Focus:</strong> Core CSA concepts</p>
            <p><strong>Level:</strong> Beginner to Intermediate</p>
            <p><strong>Topics:</strong> Service Catalog, CMDB, Workflows</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start Foundation Set", use_container_width=True):
            st.session_state.question_set = "Foundation Set"
            st.session_state.selected_questions = random.sample(questions_set1, min(questions_per_quiz, len(questions_set1)))
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()
            st.session_state.current_question = 0
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📚 Advanced Set</h3>
            <p><strong>Questions:</strong> 250</p>
            <p><strong>Focus:</strong> Advanced CSA concepts</p>
            <p><strong>Level:</strong> Intermediate to Advanced</p>
            <p><strong>Topics:</strong> Performance, Security, Integration</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("⚡ Start Advanced Set", use_container_width=True):
            st.session_state.question_set = "Advanced Set"
            st.session_state.selected_questions = random.sample(questions_set2, min(questions_per_quiz, len(questions_set2)))
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()
            st.session_state.current_question = 0
            st.rerun()
    
    st.markdown("---")
    
    # Performance History Chart
    if st.session_state.performance_history:
        st.markdown("### 📈 Learning Progress")
        
        df = pd.DataFrame(st.session_state.performance_history)
        df['date'] = pd.to_datetime(df['date'])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['date'], df['score'], marker='o', linewidth=3, markersize=8, color='#667eea')
        ax.fill_between(df['date'], df['score'], alpha=0.3, color='#667eea')
        ax.set_ylabel('Score (%)', fontsize=12, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_title('Your Learning Journey', fontsize=16, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=70, color='#ff6b6b', linestyle='--', alpha=0.7, linewidth=2, label='Passing Score (70%)')
        ax.legend(fontsize=10)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.stop()

# --------------------
# Professional Quiz Interface
# --------------------
if st.session_state.selected_questions and not st.session_state.quiz_submitted:
    total_questions = len(st.session_state.selected_questions)
    current_q = st.session_state.current_question
    question = st.session_state.selected_questions[current_q]
    
    # Timer and Progress
    elapsed_time = time.time() - st.session_state.start_time
    time_remaining = (st.session_state.quiz_time_limit * 60) - elapsed_time
    
    if time_remaining <= 0:
        st.error("⏰ Time's up! Quiz submitted automatically.")
        st.session_state.quiz_submitted = True
        st.rerun()
    
    # Professional Progress Bar
    progress = (current_q + 1) / total_questions
    st.markdown(f"""
    <div class="progress-container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <span style="font-weight: 600; color: #2c3e50;">Question {current_q + 1} of {total_questions}</span>
            <span style="font-weight: 600; color: #667eea;">{st.session_state.question_set}</span>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress*100}%;"></div>
        </div>
        <div style="text-align: center; margin-top: 0.5rem; color: #7f8c8d; font-size: 0.9rem;">
            {int(progress*100)}% Complete
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Timer
    minutes = int(time_remaining // 60)
    seconds = int(time_remaining % 60)
    st.markdown(f"""
    <div class="timer">
        ⏱️ Time Remaining: {minutes:02d}:{seconds:02d}
    </div>
    """, unsafe_allow_html=True)
    
    # Question Display
    st.markdown(f"""
    <div class="question-card">
        <h3>Q{current_q + 1}. {question['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer Options
    selected = st.multiselect(
        "Select your answer(s):",
        question["options"],
        key=f"question_{current_q}",
        default=st.session_state.user_answers.get(current_q, [])
    )
    st.session_state.user_answers[current_q] = selected
    
    # Professional Navigation
    st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("⬅️ Previous", disabled=current_q == 0):
            st.session_state.current_question = max(0, current_q - 1)
            st.rerun()
    
    with col2:
        if st.button("Next ➡️", disabled=current_q == total_questions - 1):
            st.session_state.current_question = min(total_questions - 1, current_q + 1)
            st.rerun()
    
    with col3:
        if st.button("📋 Review All"):
            st.session_state.quiz_submitted = True
            st.rerun()
    
    with col4:
        if st.button("🔄 Restart"):
            st.session_state.clear()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Study Mode - Professional Feedback
    if study_mode and selected:
        st.markdown("---")
        st.markdown("### 📖 Learning Feedback")
        
        correct_ans = question['answer']
        correct_ans = correct_ans if isinstance(correct_ans, list) else [correct_ans]
        is_correct = sorted(selected) == sorted(correct_ans)
        
        if is_correct:
            st.markdown("""
            <div class="question-card success-card">
                <h4 style="color: #00d4aa;">✅ Correct Answer!</h4>
                <p style="color: #2c3e50; margin-bottom: 1rem;"><strong>Explanation:</strong></p>
                <p style="color: #7f8c8d; line-height: 1.6;">{}</p>
            </div>
            """.format(question.get('explanation', 'No explanation available.')), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="question-card error-card">
                <h4 style="color: #ff595e;">❌ Incorrect Answer</h4>
                <p style="color: #2c3e50; margin-bottom: 0.5rem;"><strong>Your Answer:</strong> {}</p>
                <p style="color: #2c3e50; margin-bottom: 1rem;"><strong>Correct Answer:</strong> {}</p>
                <p style="color: #2c3e50; margin-bottom: 1rem;"><strong>Explanation:</strong></p>
                <p style="color: #7f8c8d; line-height: 1.6;">{}</p>
            </div>
            """.format(selected if selected else 'No answer', correct_ans, question.get('explanation', 'No explanation available.')), unsafe_allow_html=True)

# --------------------
# Professional Results Dashboard
# --------------------
if st.session_state.quiz_submitted and st.session_state.selected_questions:
    end_time = time.time()
    total_time = end_time - st.session_state.start_time
    
    correct = 0
    wrong = 0
    results = []
    
    for idx, q in enumerate(st.session_state.selected_questions):
        user_ans = st.session_state.user_answers.get(idx) or []
        correct_ans = q['answer']
        correct_ans = correct_ans if isinstance(correct_ans, list) else [correct_ans]
        is_correct = sorted(user_ans) == sorted(correct_ans)
        
        if is_correct:
            correct += 1
        else:
            wrong += 1
        
        results.append({
            "question": q['question'],
            "user_answer": user_ans,
            "correct_answer": correct_ans,
            "is_correct": is_correct,
            "explanation": q.get('explanation', 'No explanation available.')
        })
    
    # Calculate score
    percentage = (correct / len(st.session_state.selected_questions)) * 100
    
    # Save to performance history
    performance_record = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'score': percentage,
        'correct': correct,
        'total': len(st.session_state.selected_questions),
        'time_taken': total_time,
        'question_set': st.session_state.question_set
    }
    st.session_state.performance_history.append(performance_record)
    
    # Professional Results Header
    st.markdown("""
    <div class="results-header">
        <h1>🏆 Performance Report</h1>
        <p>Comprehensive analysis of your learning progress and performance metrics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Score visualization
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        # Professional Donut Chart
        fig, ax = plt.subplots(figsize=(8, 8))
        size = 0.3
        
        if percentage >= 90:
            color = '#00d4aa'
            grade = "A+"
            grade_color = '#00b894'
        elif percentage >= 80:
            color = '#00d4aa'
            grade = "A"
            grade_color = '#00b894'
        elif percentage >= 70:
            color = '#7ED957'
            grade = "B"
            grade_color = '#6c5ce7'
        elif percentage >= 60:
            color = '#FFBD59'
            grade = "C"
            grade_color = '#fdcb6e'
        elif percentage >= 50:
            color = '#FF8C42'
            grade = "D"
            grade_color = '#e17055'
        else:
            color = '#FF595E'
            grade = "F"
            grade_color = '#d63031'
        
        ax.pie(
            [correct, len(st.session_state.selected_questions) - correct],
            radius=1,
            colors=[color, '#ecf0f1'],
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=size, edgecolor='white', linewidth=2)
        )
        
        ax.text(0, 0.2, f"{int(percentage)}%", ha='center', va='center', fontsize=24, fontweight='bold', color='#2c3e50')
        ax.text(0, -0.1, f"Grade: {grade}", ha='center', va='center', fontsize=16, fontweight='bold', color=grade_color)
        ax.set(aspect="equal")
        
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("## 📊 Performance Summary")
        
        # Professional Metrics
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("🎯 Score", f"{percentage:.1f}%", f"{percentage-50:.1f}%" if percentage > 50 else f"{percentage-50:.1f}%")
            st.metric("✅ Correct", correct, f"+{correct}" if correct > 0 else f"{correct}")
        
        with col_b:
            minutes = int(total_time // 60)
            seconds = int(total_time % 60)
            st.metric("⏱️ Time", f"{minutes}m {seconds}s")
            st.metric("📚 Set", st.session_state.question_set)
        
        # Professional Insights
        st.markdown("### 💡 Performance Analysis")
        if percentage >= 90:
            st.success("🌟 Outstanding Performance! You demonstrate exceptional mastery of the material.")
        elif percentage >= 80:
            st.success("🎉 Excellent! You have a strong command of the concepts.")
        elif percentage >= 70:
            st.info("👍 Good Progress! You're well on your way to certification success.")
        elif percentage >= 60:
            st.warning("⚠️ Developing Skills. Focus on the areas you missed for improvement.")
        else:
            st.error("📚 Needs Improvement. Review the explanations carefully and consider additional study.")
        
        # Speed analysis
        time_per_q = total_time / len(st.session_state.selected_questions)
        if time_per_q < 60:
            speed_rating = "⚡ Fast"
        elif time_per_q < 120:
            speed_rating = "⏱️ Moderate"
        else:
            speed_rating = "🐌 Slow"
        
        st.info(f"**Speed Analysis:** {speed_rating} ({time_per_q:.1f} seconds per question)")
    
    with col3:
        st.markdown("## 🏆 Quick Stats")
        
        st.markdown(f"""
        <div class="custom-metric">
            <h4>Accuracy</h4>
            <h2>{percentage:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="custom-metric">
            <h4>Speed</h4>
            <h2>{time_per_q:.1f}s</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="custom-metric">
            <h4>Efficiency</h4>
            <h2>{correct}/{len(st.session_state.selected_questions)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Professional Review Section
    st.markdown("---")
    st.markdown("## 📋 Comprehensive Review")
    
    # Professional Filter Section
    st.markdown("""
    <div class="filter-section">
        <h4 style="margin-bottom: 1rem;">🔍 Review Options</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        show_correct = st.checkbox("✅ Show Correct Answers", value=True)
    with col2:
        show_incorrect = st.checkbox("❌ Show Incorrect Answers", value=True)
    with col3:
        show_all = st.checkbox("📋 Show All", value=True)
    
    # Display results with professional styling
    for idx, res in enumerate(results):
        if (show_all or 
            (show_correct and res['is_correct']) or 
            (show_incorrect and not res['is_correct'])):
            
            status = "✅ Correct" if res['is_correct'] else "❌ Incorrect"
            card_class = "success-card" if res['is_correct'] else "error-card"
            
            st.markdown(f"""
            <div class="question-card {card_class}">
                <h4 style="margin-bottom: 1rem;">Q{idx+1}: {status}</h4>
                <p style="color: #2c3e50; margin-bottom: 1rem;"><strong>Question:</strong> {res['question']}</p>
                <p style="color: #2c3e50; margin-bottom: 0.5rem;"><strong>Your Answer:</strong> {res['user_answer'] if res['user_answer'] else 'No answer'}</p>
                <p style="color: #2c3e50; margin-bottom: 1rem;"><strong>Correct Answer:</strong> {res['correct_answer']}</p>
                <p style="color: #2c3e50; margin-bottom: 0.5rem;"><strong>Explanation:</strong></p>
                <p style="color: #7f8c8d; line-height: 1.6;">{res['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Professional Action Buttons
    st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Take Another Quiz", use_container_width=True):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.rerun()
    
    with col2:
        if st.button("📊 View Analytics", use_container_width=True):
            st.session_state.show_history = True
            st.rerun()
    
    with col3:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.clear()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Professional Performance History View
if st.session_state.get('show_history', False) and st.session_state.performance_history:
    st.markdown("## 📈 Advanced Analytics Dashboard")
    
    df = pd.DataFrame(st.session_state.performance_history)
    df['date'] = pd.to_datetime(df['date'])
    
    # Professional Summary Statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="custom-metric">
            <h4>Total Quizzes</h4>
            <h2>{}</h2>
        </div>
        """.format(len(df)), unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="custom-metric">
            <h4>Average Score</h4>
            <h2>{:.1f}%</h2>
        </div>
        """.format(df['score'].mean()), unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="custom-metric">
            <h4>Best Score</h4>
            <h2>{:.1f}%</h2>
        </div>
        """.format(df['score'].max()), unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="custom-metric">
            <h4>Total Time</h4>
            <h2>{:.1f}h</h2>
        </div>
        """.format(df['time_taken'].sum()/3600), unsafe_allow_html=True)
    
    # Professional Performance Charts
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Score trend
    ax1.plot(df['date'], df['score'], marker='o', linewidth=3, markersize=8, color='#667eea')
    ax1.fill_between(df['date'], df['score'], alpha=0.3, color='#667eea')
    ax1.set_ylabel('Score (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Score Trend Over Time', fontsize=16, fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=70, color='#ff6b6b', linestyle='--', alpha=0.7, linewidth=2, label='Passing Score (70%)')
    ax1.legend(fontsize=10)
    
    # Time per question trend
    time_per_q = df['time_taken'] / df['total']
    ax2.plot(df['date'], time_per_q, marker='s', linewidth=3, markersize=8, color='#00d4aa')
    ax2.fill_between(df['date'], time_per_q, alpha=0.3, color='#00d4aa')
    ax2.set_ylabel('Time per Question (seconds)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.set_title('Speed Trend Over Time', fontsize=16, fontweight='bold', pad=20)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Professional Detailed Table
    st.markdown("### 📋 Performance Records")
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🔙 Back to Results", use_container_width=True):
        st.session_state.show_history = False
        st.rerun()
