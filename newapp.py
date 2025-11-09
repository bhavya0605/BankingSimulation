import streamlit as st
import time
import random
import json
from datetime import datetime, timedelta

# ========================================
# GROQ API INTEGRATION
# ========================================

def call_groq_agent(agent_role, user_context, conversation_history=""):
    """
    Simulates Groq API call for agent responses
    In production: Replace with actual Groq API call
    """
    # This is a simulation - in production you'd call:
    # from groq import Groq
    # client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    prompts = {
        'sales': f"You are a friendly loan sales agent. Customer needs: {user_context}. Be persuasive and empathetic. Keep response under 50 words.",
        'verification': f"You are a verification agent. Confirm customer details professionally. Keep response under 40 words.",
        'underwriting': f"You are an underwriting agent analyzing credit worthiness. Context: {user_context}. Be technical but clear. Keep response under 60 words.",
        'master': f"You are the master orchestrator. Guide the customer to the next step. Keep response under 30 words."
    }
    
    # Simulate API delay
    time.sleep(0.5)
    
    # Return simulated response (in production, this would be actual Groq API response)
    return f"[Agent Response: {agent_role}]"

# ========================================
# MOCK DATA - 10 CUSTOMERS
# ========================================

CRM_DB = {
    'CUST001': {
        'name': 'Rohan Sharma', 'age': 32, 'city': 'Bangalore',
        'phone': '9845012301', 'email': 'rohan.sharma@email.com',
        'address': '123, MG Road, Indiranagar, Bangalore - 560038',
        'kyc_status': 'Verified', 'occupation': 'Software Engineer',
        'employer': 'Tech Corp India', 'monthly_salary': 95000,
        'existing_loans': ['Home Loan - ₹45L outstanding'],
        'relationship_since': '2019-03-15'
    },
    'CUST002': {
        'name': 'Priya Patel', 'age': 28, 'city': 'Mumbai',
        'phone': '9876543210', 'email': 'priya.p@email.com',
        'address': '456, Linking Road, Bandra West, Mumbai - 400050',
        'kyc_status': 'Verified', 'occupation': 'Marketing Manager',
        'employer': 'Brand Solutions Ltd', 'monthly_salary': 125000,
        'existing_loans': [], 'relationship_since': '2020-07-22'
    },
    'CUST003': {
        'name': 'Amit Kumar', 'age': 45, 'city': 'Delhi',
        'phone': '9810234567', 'email': 'amit.k@email.com',
        'address': '789, Janakpuri, West Delhi, Delhi - 110058',
        'kyc_status': 'Verified', 'occupation': 'Business Owner',
        'employer': 'Self Employed', 'monthly_salary': 75000,
        'existing_loans': ['Auto Loan - ₹3L outstanding', 'Personal Loan - ₹2L outstanding'],
        'relationship_since': '2018-01-10'
    },
    'CUST004': {
        'name': 'Sneha Reddy', 'age': 35, 'city': 'Hyderabad',
        'phone': '9440123456', 'email': 'sneha.reddy@email.com',
        'address': '321, Jubilee Hills, Hyderabad - 500033',
        'kyc_status': 'Verified', 'occupation': 'Architect',
        'employer': 'Design Studio Pvt Ltd', 'monthly_salary': 110000,
        'existing_loans': ['Home Loan - ₹25L outstanding'],
        'relationship_since': '2021-05-18'
    },
    'CUST005': {
        'name': 'Vikram Singh', 'age': 29, 'city': 'Pune',
        'phone': '9823456789', 'email': 'vikram.singh@email.com',
        'address': '88, Koregaon Park, Pune - 411001',
        'kyc_status': 'Verified', 'occupation': 'Data Scientist',
        'employer': 'Analytics Hub', 'monthly_salary': 105000,
        'existing_loans': [], 'relationship_since': '2022-11-03'
    },
    'CUST006': {
        'name': 'Anjali Mehta', 'age': 41, 'city': 'Ahmedabad',
        'phone': '9898765432', 'email': 'anjali.m@email.com',
        'address': '45, CG Road, Navrangpura, Ahmedabad - 380009',
        'kyc_status': 'Verified', 'occupation': 'Doctor',
        'employer': 'City Hospital', 'monthly_salary': 180000,
        'existing_loans': ['Home Loan - ₹60L outstanding'],
        'relationship_since': '2017-09-12'
    },
    'CUST007': {
        'name': 'Rahul Desai', 'age': 26, 'city': 'Chennai',
        'phone': '9840567890', 'email': 'rahul.desai@email.com',
        'address': '67, Anna Nagar, Chennai - 600040',
        'kyc_status': 'Verified', 'occupation': 'Associate Consultant',
        'employer': 'Consulting Group', 'monthly_salary': 65000,
        'existing_loans': [], 'relationship_since': '2023-02-28'
    },
    'CUST008': {
        'name': 'Kavita Rao', 'age': 38, 'city': 'Bangalore',
        'phone': '9845678901', 'email': 'kavita.rao@email.com',
        'address': '234, Whitefield, Bangalore - 560066',
        'kyc_status': 'Verified', 'occupation': 'HR Director',
        'employer': 'Global Tech Solutions', 'monthly_salary': 155000,
        'existing_loans': ['Auto Loan - ₹4L outstanding'],
        'relationship_since': '2019-08-05'
    },
    'CUST009': {
        'name': 'Sanjay Gupta', 'age': 52, 'city': 'Kolkata',
        'phone': '9830123456', 'email': 'sanjay.g@email.com',
        'address': '12, Park Street, Kolkata - 700016',
        'kyc_status': 'Verified', 'occupation': 'Senior Manager',
        'employer': 'Manufacturing Ltd', 'monthly_salary': 95000,
        'existing_loans': ['Personal Loan - ₹5L outstanding', 'Home Loan - ₹35L outstanding'],
        'relationship_since': '2016-04-20'
    },
    'CUST010': {
        'name': 'Neha Joshi', 'age': 31, 'city': 'Jaipur',
        'phone': '9829876543', 'email': 'neha.joshi@email.com',
        'address': '99, Malviya Nagar, Jaipur - 302017',
        'kyc_status': 'Verified', 'occupation': 'Teacher',
        'employer': 'International School', 'monthly_salary': 55000,
        'existing_loans': [], 'relationship_since': '2021-12-10'
    }
}

CREDIT_BUREAU_API = {
    'CUST001': 780, 'CUST002': 850, 'CUST003': 650, 'CUST004': 790, 'CUST005': 820,
    'CUST006': 875, 'CUST007': 720, 'CUST008': 810, 'CUST009': 680, 'CUST010': 740
}

OFFER_MART_API = {
    'CUST001': 300000, 'CUST002': 500000, 'CUST003': 100000, 'CUST004': 350000, 'CUST005': 400000,
    'CUST006': 750000, 'CUST007': 150000, 'CUST008': 600000, 'CUST009': 200000, 'CUST010': 180000
}

INTEREST_RATES = {
    'excellent': {'range': '850-900', 'rate': 10.5},
    'very_good': {'range': '800-849', 'rate': 11.5},
    'good': {'range': '750-799', 'rate': 12.5},
    'fair': {'range': '700-749', 'rate': 14.0},
    'poor': {'range': '<700', 'rate': 16.5}
}

# ========================================
# HELPER FUNCTIONS
# ========================================

def initialize_session():
    defaults = {
        'stage': 'LOGIN',
        'messages': [],
        'user_id': None,
        'loan_amount': None,
        'loan_tenure': None,
        'interest_rate': None,
        'monthly_emi': None,
        'purpose': None,
        'address_verified': False,
        'salary_slip_uploaded': False,
        'active_agent': None
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def add_message(agent, message):
    st.session_state.messages.append({
        'agent': agent,
        'message': message,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    })

def calculate_emi(principal, rate, tenure_months):
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (((1 + monthly_rate) ** tenure_months) - 1)
    return round(emi, 2)

def get_interest_rate(credit_score):
    if credit_score >= 850: return INTEREST_RATES['excellent']['rate']
    elif credit_score >= 800: return INTEREST_RATES['very_good']['rate']
    elif credit_score >= 750: return INTEREST_RATES['good']['rate']
    elif credit_score >= 700: return INTEREST_RATES['fair']['rate']
    else: return INTEREST_RATES['poor']['rate']

def get_agent_avatar(agent_name):
    avatars = {
        'MasterAgent': '🎯',
        'SalesAgent': '💼',
        'VerificationAgent': '🔍',
        'UnderwritingAgent': '📊',
        'SanctionLetterGenerator': '📄',
        'User': '👤'
    }
    return avatars.get(agent_name, '💬')

# ========================================
# MAIN APP
# ========================================

def main():
    st.set_page_config(
        page_title="Tata Capital Loan Assistant",
        page_icon="🏦",
        layout="wide"
    )
    
    # Custom CSS for cleaner UI
    st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 2rem;
        }
        .main-header h1 {
            color: white;
            margin: 0;
            font-size: 2.5rem;
        }
        .main-header p {
            color: #e0e0e0;
            margin: 0.5rem 0 0 0;
        }
        .agent-status {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .active-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .active { background-color: #28a745; }
        .standby { background-color: #ffc107; }
        .inactive { background-color: #6c757d; }
        </style>
    """, unsafe_allow_html=True)
    
    initialize_session()
    
    # ========================================
    # SIDEBAR - Cleaner Design
    # ========================================
    with st.sidebar:
        st.markdown("### 🎯 Agent Status")
        
        if st.session_state.user_id:
            user_data = CRM_DB[st.session_state.user_id]
            
            # Active agent indicator
            agents = {
                'MasterAgent': '🤖 Master',
                'SalesAgent': '💼 Sales',
                'VerificationAgent': '🔍 Verification',
                'UnderwritingAgent': '📊 Underwriting',
                'SanctionLetterGenerator': '📄 Document Gen'
            }
            
            for agent_key, agent_name in agents.items():
                status_class = 'active' if st.session_state.active_agent == agent_key else 'standby'
                status_text = '🟢 Active' if st.session_state.active_agent == agent_key else '⚪ Standby'
                st.markdown(f"**{agent_name}**: {status_text}")
            
            st.divider()
            
            # Customer info (collapsed by default for cleaner look)
            with st.expander("👤 Customer Profile"):
                st.write(f"**{user_data['name']}**")
                st.caption(f"{user_data['city']} • {user_data['occupation']}")
                st.metric("Credit Score", f"{CREDIT_BUREAU_API[st.session_state.user_id]}/900")
                st.metric("Pre-approved", f"₹{OFFER_MART_API[st.session_state.user_id]:,}")
        else:
            st.info("👋 Please log in to start")
        
        st.divider()
        
        if st.button("🔄 Reset", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # ========================================
    # MAIN CONTENT
    # ========================================
    
    # Cleaner header
    st.markdown("""
        <div class="main-header">
            <h1>🏦 Tata Capital AI Loan Assistant</h1>
            <p>Powered by Agentic AI • Instant Loan Approvals</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ========================================
    # STAGE: LOGIN
    # ========================================
    if st.session_state.stage == 'LOGIN':
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("### 🎯 Get Started")
            st.write("Select your profile to continue")
            
            user_options = {uid: f"{data['name']} • {data['city']}" for uid, data in CRM_DB.items()}
            selected_user = st.selectbox(
                "Customer Profile",
                options=[''] + list(user_options.keys()),
                format_func=lambda x: 'Choose your profile...' if x == '' else user_options.get(x, x),
                label_visibility="collapsed"
            )
            
            if selected_user:
                user_data = CRM_DB[selected_user]
                
                # Quick preview
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Credit Score", f"{CREDIT_BUREAU_API[selected_user]}/900")
                with col_b:
                    st.metric("Pre-approved Limit", f"₹{OFFER_MART_API[selected_user]/100000:.1f}L")
                
                if st.button("🚀 Start Application", type="primary", use_container_width=True):
                    st.session_state.user_id = selected_user
                    st.session_state.stage = 'WELCOME'
                    st.session_state.active_agent = 'MasterAgent'
                    
                    pre_approved = OFFER_MART_API[selected_user]
                    
                    add_message("MasterAgent", f"Hello {user_data['name']}! 👋 I'm your AI loan assistant.")
                    add_message("MasterAgent", f"Great news! You have a pre-approved offer of ₹{pre_approved:,} 🎉")
                    add_message("MasterAgent", "Connecting you with our Sales team...")
                    
                    st.rerun()
    
    # ========================================
    # CONVERSATION DISPLAY
    # ========================================
    if st.session_state.stage != 'LOGIN':
        chat_container = st.container()
        
        with chat_container:
            for msg in st.session_state.messages:
                avatar = get_agent_avatar(msg['agent'])
                
                with st.chat_message(msg['agent'], avatar=avatar):
                    st.markdown(msg['message'])
                    st.caption(f"🕒 {msg['timestamp']}")
        
        # ========================================
        # STAGE: WELCOME
        # ========================================
        if st.session_state.stage == 'WELCOME':
            time.sleep(1)
            st.session_state.active_agent = 'SalesAgent'
            add_message("SalesAgent", f"Hi! I'm your Sales Agent. Let's find the perfect loan for you! 💼")
            st.session_state.stage = 'DISCOVER_NEEDS'
            st.rerun()
        
        # ========================================
        # STAGE: DISCOVER NEEDS
        # ========================================
        elif st.session_state.stage == 'DISCOVER_NEEDS':
            with st.chat_message("SalesAgent", avatar="💼"):
                st.write("**What will you use this loan for?**")
                
                purposes = [
                    "🏠 Home Renovation", "💒 Wedding", "📚 Education", "🏥 Medical",
                    "🚗 Vehicle", "💼 Business", "✈️ Travel", "💳 Debt Consolidation"
                ]
                
                purpose = st.selectbox("Loan Purpose", purposes, label_visibility="collapsed")
                
                if st.button("Continue", type="primary"):
                    st.session_state.purpose = purpose
                    add_message("User", purpose)
                    add_message("SalesAgent", f"Perfect! Let's customize your loan offer.")
                    st.session_state.stage = 'LOAN_DETAILS'
                    st.rerun()
        
        # ========================================
        # STAGE: LOAN DETAILS
        # ========================================
        elif st.session_state.stage == 'LOAN_DETAILS':
            pre_approved = OFFER_MART_API[st.session_state.user_id]
            
            with st.chat_message("SalesAgent", avatar="💼"):
                col1, col2 = st.columns(2)
                
                with col1:
                    loan_amount = st.number_input(
                        "💰 Amount (₹)",
                        min_value=25000,
                        max_value=2000000,
                        value=min(200000, pre_approved),
                        step=25000
                    )
                
                with col2:
                    tenure = st.selectbox(
                        "📅 Tenure",
                        options=[12, 24, 36, 48, 60],
                        format_func=lambda x: f"{x//12}Y" if x >= 12 else f"{x}M",
                        index=2
                    )
                
                # EMI calculation
                credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
                interest_rate = get_interest_rate(credit_score)
                emi = calculate_emi(loan_amount, interest_rate, tenure)
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Monthly EMI", f"₹{emi:,.0f}")
                col2.metric("Interest Rate", f"{interest_rate}%")
                col3.metric("Total Payment", f"₹{emi * tenure:,.0f}")
                
                if st.button("✅ Proceed", type="primary", use_container_width=True):
                    st.session_state.loan_amount = loan_amount
                    st.session_state.loan_tenure = tenure
                    st.session_state.interest_rate = interest_rate
                    st.session_state.monthly_emi = emi
                    
                    add_message("User", f"₹{loan_amount:,} for {tenure} months")
                    add_message("SalesAgent", f"Great! EMI: ₹{emi:,.0f}/month")
                    add_message("MasterAgent", "Transferring to Verification...")
                    st.session_state.active_agent = 'VerificationAgent'
                    st.session_state.stage = 'VERIFICATION'
                    st.rerun()
        
        # ========================================
        # STAGE: VERIFICATION
        # ========================================
        elif st.session_state.stage == 'VERIFICATION':
            if not st.session_state.address_verified:
                time.sleep(1)
                add_message("VerificationAgent", "Checking your details... 🔍")
                time.sleep(1)
                
                user_data = CRM_DB[st.session_state.user_id]
                add_message("VerificationAgent", f"✅ KYC Verified")
                
                with st.chat_message("VerificationAgent", avatar="🔍"):
                    st.info(f"📍 {user_data['address']}")
                    st.write("Is this correct?")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("✅ Yes", type="primary", use_container_width=True):
                            st.session_state.address_verified = True
                            add_message("User", "Confirmed")
                            add_message("VerificationAgent", "Verified! ✓")
                            add_message("MasterAgent", "Moving to Underwriting...")
                            st.session_state.active_agent = 'UnderwritingAgent'
                            st.session_state.stage = 'UNDERWRITING'
                            st.rerun()
                    
                    with col2:
                        if st.button("❌ Update Required", use_container_width=True):
                            add_message("VerificationAgent", "Please contact support to update details.")
                            st.session_state.stage = 'END'
                            st.rerun()
        
        # ========================================
        # STAGE: UNDERWRITING
        # ========================================
        elif st.session_state.stage == 'UNDERWRITING':
            time.sleep(1)
            add_message("UnderwritingAgent", "Analyzing your application... 📊")
            
            with st.spinner("Fetching credit report..."):
                time.sleep(2)
            
            credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
            pre_approved = OFFER_MART_API[st.session_state.user_id]
            loan_amount = st.session_state.loan_amount
            
            add_message("UnderwritingAgent", f"Credit Score: {credit_score}/900")
            
            # Decision logic
            if loan_amount <= pre_approved and credit_score >= 700:
                st.session_state.stage = 'APPROVED'
            elif pre_approved < loan_amount <= 2 * pre_approved and credit_score >= 700:
                st.session_state.stage = 'SALARY_SLIP'
            else:
                st.session_state.stage = 'REJECTED'
            
            st.rerun()
        
        # ========================================
        # STAGE: APPROVED
        # ========================================
        elif st.session_state.stage == 'APPROVED':
            add_message("UnderwritingAgent", "🎉 APPROVED!")
            add_message("MasterAgent", "Generating sanction letter...")
            st.session_state.active_agent = 'SanctionLetterGenerator'
            st.session_state.stage = 'GENERATE_LETTER'
            st.rerun()
        
        # ========================================
        # STAGE: SALARY SLIP
        # ========================================
        elif st.session_state.stage == 'SALARY_SLIP':
            if not st.session_state.salary_slip_uploaded:
                add_message("UnderwritingAgent", "Please upload your salary slip for verification 📄")
                
                with st.chat_message("UnderwritingAgent", avatar="📊"):
                    uploaded_file = st.file_uploader("Upload Document", type=['pdf', 'jpg', 'png'])
                    
                    if uploaded_file and st.button("Submit", type="primary"):
                        with st.spinner("Verifying..."):
                            time.sleep(2)
                        
                        add_message("UnderwritingAgent", "✅ Verified! Loan APPROVED! 🎉")
                        st.session_state.salary_slip_uploaded = True
                        st.session_state.stage = 'APPROVED'
                        st.rerun()
        
        # ========================================
        # STAGE: REJECTED
        # ========================================
        elif st.session_state.stage == 'REJECTED':
            pre_approved = OFFER_MART_API[st.session_state.user_id]
            
            add_message("UnderwritingAgent", "Unable to approve requested amount.")
            add_message("MasterAgent", f"Alternative: ₹{pre_approved:,} available")
            
            with st.chat_message("MasterAgent", avatar="🎯"):
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Accept", type="primary", use_container_width=True):
                        st.session_state.loan_amount = pre_approved
                        st.session_state.stage = 'APPROVED'
                        st.rerun()
                with col2:
                    if st.button("❌ Cancel", use_container_width=True):
                        st.session_state.stage = 'END'
                        st.rerun()
        
        # ========================================
        # STAGE: GENERATE LETTER
        # ========================================
        elif st.session_state.stage == 'GENERATE_LETTER':
            with st.spinner("Generating document..."):
                time.sleep(2)
            
            user_data = CRM_DB[st.session_state.user_id]
            loan_id = f"TC{random.randint(10000, 99999)}"
            
            add_message("SanctionLetterGenerator", "✅ Letter Generated!")
            
            with st.chat_message("SanctionLetterGenerator", avatar="📄"):
                st.success("🎉 **LOAN APPROVED**")
                
                st.markdown(f"""
                **Loan ID:** {loan_id}  
                **Customer:** {user_data['name']}  
                **Amount:** ₹{st.session_state.loan_amount:,}  
                **EMI:** ₹{st.session_state.monthly_emi:,.0f}  
                **Tenure:** {st.session_state.loan_tenure} months  
                **Rate:** {st.session_state.interest_rate}% p.a.
                """)
                
                st.download_button(
                    "📥 Download",
                    data="Sanction Letter",
                    file_name=f"Loan_{loan_id}.pdf",
                    use_container_width=True
                )
                
                st.balloons()
            
            # Success message and future improvements
            time.sleep(1)
            add_message("MasterAgent", "🎊 Congratulations on your loan approval!")
            
            with st.chat_message("MasterAgent", avatar="🎯"):
                st.success("✅ **Application Complete!**")
                st.write("---")
                
                # Future improvements section
                st.markdown("### 🚀 **Future Enhancements for Production**")
                
                with st.expander("🤖 **AI & Intelligence Upgrades**", expanded=True):
                    st.markdown("""
                    - **Real LLM Integration**: Connect with Groq/Claude/GPT for dynamic, context-aware conversations
                    - **Sentiment Analysis**: Detect customer emotions and adapt agent tone accordingly
                    - **Predictive Analytics**: ML models to predict loan approval probability upfront
                    - **Smart Recommendations**: AI suggests optimal loan amount, tenure based on financial profile
                    - **Voice Interface**: Add speech-to-text for voice-based loan applications
                    - **Multi-language Support**: Support for 10+ Indian languages using NLP
                    """)
                
                with st.expander("🔗 **Integration & Automation**"):
                    st.markdown("""
                    - **Real-time Credit Bureau APIs**: CIBIL, Experian, Equifax integration
                    - **Bank Statement Analysis**: OCR + AI to analyze uploaded bank statements automatically
                    - **Income Verification**: Integration with ITR portal, Form 16 verification
                    - **Digital KYC**: Aadhaar-based eKYC, Video KYC for instant verification
                    - **CRM Integration**: Salesforce, Zoho for seamless customer management
                    - **Payment Gateway**: Automated EMI collection via UPI, NACH
                    - **E-signature**: DocuSign/Aadhaar eSign for instant document signing
                    """)
                
                with st.expander("📊 **Analytics & Insights**"):
                    st.markdown("""
                    - **Conversion Funnel**: Track drop-off points and optimize user journey
                    - **A/B Testing**: Test different conversation flows for better conversion
                    - **Customer Dashboard**: Real-time loan status, EMI tracker, prepayment calculator
                    - **Agent Performance**: Monitor which AI agents perform best, optimize prompts
                    - **Fraud Detection**: ML models to detect suspicious applications
                    - **Risk Scoring**: Advanced credit risk models beyond credit score
                    """)
                
                with st.expander("💼 **Business Features**"):
                    st.markdown("""
                    - **Dynamic Pricing**: Real-time interest rate adjustments based on market conditions
                    - **Cross-sell/Upsell**: Recommend insurance, credit cards during application
                    - **Loyalty Program**: Better rates for existing customers, referral bonuses
                    - **Co-applicant Support**: Add co-borrowers to increase eligibility
                    - **Balance Transfer**: Help customers transfer from other banks
                    - **Top-up Loans**: Offer additional loans to existing customers
                    """)
                
                with st.expander("🛡️ **Security & Compliance**"):
                    st.markdown("""
                    - **End-to-end Encryption**: All data encrypted at rest and in transit
                    - **OAuth 2.0**: Secure authentication with 2FA
                    - **Audit Logging**: Complete trail of all actions for compliance
                    - **GDPR/Data Privacy**: Full compliance with data protection laws
                    - **PCI DSS**: Payment card security standards
                    - **Regular Penetration Testing**: Security audits and vulnerability assessments
                    - **Role-based Access Control**: Different permissions for agents, managers
                    """)
                
                with st.expander("📱 **User Experience**"):
                    st.markdown("""
                    - **Mobile App**: Native iOS/Android apps with better UX
                    - **Progressive Web App**: Installable web app, offline support
                    - **WhatsApp Integration**: Apply for loans via WhatsApp chatbot
                    - **SMS Notifications**: Real-time updates at each stage
                    - **Email Journey**: Automated email sequences
                    - **Video KYC**: Face-to-face verification via video call
                    - **Chat History**: Save and resume applications anytime
                    - **Dark Mode**: Eye-friendly interface for late-night applications
                    """)
                
                with st.expander("⚡ **Performance & Scale**"):
                    st.markdown("""
                    - **Microservices Architecture**: Independent scaling of each agent
                    - **Load Balancing**: Handle millions of concurrent users
                    - **CDN Integration**: Fast loading globally
                    - **Caching Strategy**: Redis for frequently accessed data
                    - **Async Processing**: Queue-based processing for heavy operations
                    - **Auto-scaling**: Scale up/down based on demand
                    - **99.99% Uptime**: High availability with redundancy
                    """)
                
                st.write("---")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Current Processing Time", "~3 mins", delta="⚡ Fast")
                with col2:
                    st.metric("With Full AI", "~30 secs", delta="90% faster")
                with col3:
                    st.metric("Scalability", "∞", delta="Cloud-native")
                
                st.info("💡 **This prototype demonstrates the core agentic architecture. All features above can be built on this foundation!**")
            
            st.session_state.active_agent = 'MasterAgent'
            st.session_state.stage = 'END'
        
        # ========================================
        # STAGE: END
        # ========================================
        elif st.session_state.stage == 'END':
            with st.chat_message("MasterAgent", avatar="🎯"):
                st.write("Thank you for choosing Tata Capital! 🙏")
                
                if st.button("🏠 New Application", use_container_width=True):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.rerun()
    
    # Footer
    st.divider()
    st.caption("🔒 Tata Capital © 2024 | Powered by Agentic AI")

if __name__ == "__main__":
    main()