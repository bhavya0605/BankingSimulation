import streamlit as st
import time
import random
from datetime import datetime, timedelta

# ========================================
# MOCK DATA - 10 CUSTOMERS
# ========================================

CRM_DB = {
    'CUST001': {
        'name': 'Rohan Sharma',
        'age': 32,
        'city': 'Bangalore',
        'phone': '9845012301',
        'email': 'rohan.sharma@email.com',
        'address': '123, MG Road, Indiranagar, Bangalore - 560038',
        'kyc_status': 'Verified',
        'occupation': 'Software Engineer',
        'employer': 'Tech Corp India',
        'monthly_salary': 95000,
        'existing_loans': ['Home Loan - ₹45L outstanding'],
        'relationship_since': '2019-03-15'
    },
    'CUST002': {
        'name': 'Priya Patel',
        'age': 28,
        'city': 'Mumbai',
        'phone': '9876543210',
        'email': 'priya.p@email.com',
        'address': '456, Linking Road, Bandra West, Mumbai - 400050',
        'kyc_status': 'Verified',
        'occupation': 'Marketing Manager',
        'employer': 'Brand Solutions Ltd',
        'monthly_salary': 125000,
        'existing_loans': [],
        'relationship_since': '2020-07-22'
    },
    'CUST003': {
        'name': 'Amit Kumar',
        'age': 45,
        'city': 'Delhi',
        'phone': '9810234567',
        'email': 'amit.k@email.com',
        'address': '789, Janakpuri, West Delhi, Delhi - 110058',
        'kyc_status': 'Verified',
        'occupation': 'Business Owner',
        'employer': 'Self Employed',
        'monthly_salary': 75000,
        'existing_loans': ['Auto Loan - ₹3L outstanding', 'Personal Loan - ₹2L outstanding'],
        'relationship_since': '2018-01-10'
    },
    'CUST004': {
        'name': 'Sneha Reddy',
        'age': 35,
        'city': 'Hyderabad',
        'phone': '9440123456',
        'email': 'sneha.reddy@email.com',
        'address': '321, Jubilee Hills, Hyderabad - 500033',
        'kyc_status': 'Verified',
        'occupation': 'Architect',
        'employer': 'Design Studio Pvt Ltd',
        'monthly_salary': 110000,
        'existing_loans': ['Home Loan - ₹25L outstanding'],
        'relationship_since': '2021-05-18'
    },
    'CUST005': {
        'name': 'Vikram Singh',
        'age': 29,
        'city': 'Pune',
        'phone': '9823456789',
        'email': 'vikram.singh@email.com',
        'address': '88, Koregaon Park, Pune - 411001',
        'kyc_status': 'Verified',
        'occupation': 'Data Scientist',
        'employer': 'Analytics Hub',
        'monthly_salary': 105000,
        'existing_loans': [],
        'relationship_since': '2022-11-03'
    },
    'CUST006': {
        'name': 'Anjali Mehta',
        'age': 41,
        'city': 'Ahmedabad',
        'phone': '9898765432',
        'email': 'anjali.m@email.com',
        'address': '45, CG Road, Navrangpura, Ahmedabad - 380009',
        'kyc_status': 'Verified',
        'occupation': 'Doctor',
        'employer': 'City Hospital',
        'monthly_salary': 180000,
        'existing_loans': ['Home Loan - ₹60L outstanding'],
        'relationship_since': '2017-09-12'
    },
    'CUST007': {
        'name': 'Rahul Desai',
        'age': 26,
        'city': 'Chennai',
        'phone': '9840567890',
        'email': 'rahul.desai@email.com',
        'address': '67, Anna Nagar, Chennai - 600040',
        'kyc_status': 'Verified',
        'occupation': 'Associate Consultant',
        'employer': 'Consulting Group',
        'monthly_salary': 65000,
        'existing_loans': [],
        'relationship_since': '2023-02-28'
    },
    'CUST008': {
        'name': 'Kavita Rao',
        'age': 38,
        'city': 'Bangalore',
        'phone': '9845678901',
        'email': 'kavita.rao@email.com',
        'address': '234, Whitefield, Bangalore - 560066',
        'kyc_status': 'Verified',
        'occupation': 'HR Director',
        'employer': 'Global Tech Solutions',
        'monthly_salary': 155000,
        'existing_loans': ['Auto Loan - ₹4L outstanding'],
        'relationship_since': '2019-08-05'
    },
    'CUST009': {
        'name': 'Sanjay Gupta',
        'age': 52,
        'city': 'Kolkata',
        'phone': '9830123456',
        'email': 'sanjay.g@email.com',
        'address': '12, Park Street, Kolkata - 700016',
        'kyc_status': 'Verified',
        'occupation': 'Senior Manager',
        'employer': 'Manufacturing Ltd',
        'monthly_salary': 95000,
        'existing_loans': ['Personal Loan - ₹5L outstanding', 'Home Loan - ₹35L outstanding'],
        'relationship_since': '2016-04-20'
    },
    'CUST010': {
        'name': 'Neha Joshi',
        'age': 31,
        'city': 'Jaipur',
        'phone': '9829876543',
        'email': 'neha.joshi@email.com',
        'address': '99, Malviya Nagar, Jaipur - 302017',
        'kyc_status': 'Verified',
        'occupation': 'Teacher',
        'employer': 'International School',
        'monthly_salary': 55000,
        'existing_loans': [],
        'relationship_since': '2021-12-10'
    }
}

CREDIT_BUREAU_API = {
    'CUST001': 780,
    'CUST002': 850,
    'CUST003': 650,
    'CUST004': 790,
    'CUST005': 820,
    'CUST006': 875,
    'CUST007': 720,
    'CUST008': 810,
    'CUST009': 680,
    'CUST010': 740
}

OFFER_MART_API = {
    'CUST001': 300000,
    'CUST002': 500000,
    'CUST003': 100000,
    'CUST004': 350000,
    'CUST005': 400000,
    'CUST006': 750000,
    'CUST007': 150000,
    'CUST008': 600000,
    'CUST009': 200000,
    'CUST010': 180000
}

# Interest rate tiers based on credit score
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
    """Initialize session state variables"""
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
        'negotiation_count': 0,
        'offer_accepted': False,
        'agent_thinking': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def add_message(agent, message, thinking=False):
    """Add a message to the conversation history"""
    st.session_state.messages.append({
        'agent': agent,
        'message': message,
        'timestamp': datetime.now().strftime("%H:%M:%S"),
        'thinking': thinking
    })

def calculate_emi(principal, rate, tenure_months):
    """Calculate EMI using reducing balance method"""
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (((1 + monthly_rate) ** tenure_months) - 1)
    return round(emi, 2)

def get_interest_rate(credit_score):
    """Get interest rate based on credit score"""
    if credit_score >= 850:
        return INTEREST_RATES['excellent']['rate']
    elif credit_score >= 800:
        return INTEREST_RATES['very_good']['rate']
    elif credit_score >= 750:
        return INTEREST_RATES['good']['rate']
    elif credit_score >= 700:
        return INTEREST_RATES['fair']['rate']
    else:
        return INTEREST_RATES['poor']['rate']

def simulate_typing(text, container):
    """Simulate typing effect"""
    placeholder = container.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(0.01)

def get_agent_avatar(agent_name):
    """Return emoji avatar for each agent"""
    avatars = {
        'MasterAgent': '🤖',
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
    # Page config
    st.set_page_config(
        page_title="Tata Capital Loan Assistant",
        page_icon="🏦",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .agent-badge {
            background-color: #f0f2f6;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
        }
        .success-box {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        .warning-box {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
        <div class="main-header">
            <h1>🏦 Tata Capital - AI Loan Assistant</h1>
            <p>Powered by Agentic AI | Your Personal Loan Journey Starts Here</p>
        </div>
    """, unsafe_allow_html=True)
    
    initialize_session()
    
    # Sidebar - Customer Info & Stats
    with st.sidebar:
        st.title("📊 Dashboard")
        
        if st.session_state.user_id:
            user_data = CRM_DB[st.session_state.user_id]
            st.success(f"**Logged in as:** {user_data['name']}")
            
            with st.expander("👤 Profile Details", expanded=True):
                st.write(f"**City:** {user_data['city']}")
                st.write(f"**Occupation:** {user_data['occupation']}")
                st.write(f"**Monthly Salary:** ₹{user_data['monthly_salary']:,}")
                st.write(f"**Customer Since:** {user_data['relationship_since']}")
            
            if st.session_state.user_id in CREDIT_BUREAU_API:
                credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
                st.metric("Credit Score", f"{credit_score}/900")
                
                pre_approved = OFFER_MART_API[st.session_state.user_id]
                st.metric("Pre-approved Limit", f"₹{pre_approved:,}")
        
        st.divider()
        
        st.subheader("🤖 Active Agents")
        agents_status = {
            'Master Agent': '🟢 Active',
            'Sales Agent': '🟡 Standby',
            'Verification Agent': '🟡 Standby',
            'Underwriting Agent': '🟡 Standby',
            'Sanction Generator': '🟡 Standby'
        }
        
        for agent, status in agents_status.items():
            st.text(f"{agent}: {status}")
        
        st.divider()
        
        if st.button("🔄 Reset Session", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # ========================================
    # STAGE: LOGIN
    # ========================================
    if st.session_state.stage == 'LOGIN':
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("### 👋 Welcome Back!")
            st.write("Please select your profile to continue with your loan application")
            
            user_options = {uid: f"{data['name']} ({data['city']})" for uid, data in CRM_DB.items()}
            selected_user = st.selectbox(
                "Select Customer Profile:",
                options=[''] + list(user_options.keys()),
                format_func=lambda x: 'Choose your profile...' if x == '' else user_options.get(x, x),
                key='user_select'
            )
            
            if selected_user:
                user_data = CRM_DB[selected_user]
                with st.expander("Preview Profile Details"):
                    st.write(f"**Name:** {user_data['name']}")
                    st.write(f"**Age:** {user_data['age']} years")
                    st.write(f"**City:** {user_data['city']}")
                    st.write(f"**Occupation:** {user_data['occupation']}")
                    st.write(f"**Pre-approved Limit:** ₹{OFFER_MART_API[selected_user]:,}")
                    st.write(f"**Credit Score:** {CREDIT_BUREAU_API[selected_user]}/900")
                
                if st.button("🚀 Start Loan Journey", type="primary", use_container_width=True):
                    st.session_state.user_id = selected_user
                    st.session_state.stage = 'WELCOME'
                    st.session_state.messages = []
                    
                    user_data = CRM_DB[selected_user]
                    pre_approved = OFFER_MART_API[selected_user]
                    
                    # Initial greeting from Master Agent
                    add_message("MasterAgent", f"Hello {user_data['name']}! 👋 Welcome to Tata Capital. I'm your AI assistant, and I'm here to help you with your personal loan needs.")
                    time.sleep(0.5)
                    add_message("MasterAgent", f"I see you've been a valued customer since {user_data['relationship_since']}. Thank you for your continued trust! 🙏")
                    time.sleep(0.5)
                    add_message("MasterAgent", f"Great news! Based on your profile, you have a **pre-approved personal loan offer of ₹{pre_approved:,}** with attractive interest rates! 🎉")
                    time.sleep(0.5)
                    add_message("MasterAgent", "Let me connect you with our Sales specialist who will guide you through the entire process. One moment please...")
                    
                    st.rerun()
    
    # ========================================
    # DISPLAY CONVERSATION
    # ========================================
    if st.session_state.stage != 'LOGIN':
        # Chat container
        chat_container = st.container()
        
        with chat_container:
            for idx, msg in enumerate(st.session_state.messages):
                avatar = get_agent_avatar(msg['agent'])
                
                with st.chat_message(msg['agent'], avatar=avatar):
                    if msg.get('thinking', False):
                        st.markdown(f"*{msg['message']}*")
                    else:
                        st.markdown(msg['message'])
                    st.caption(f"🕒 {msg['timestamp']}")
        
        # ========================================
        # STAGE: WELCOME - Sales Agent Introduction
        # ========================================
        if st.session_state.stage == 'WELCOME':
            time.sleep(1)
            add_message("SalesAgent", f"Hi {CRM_DB[st.session_state.user_id]['name']}! I'm your dedicated Sales Agent. I'm here to understand your financial needs and help you get the best loan offer. 💼")
            time.sleep(0.5)
            add_message("SalesAgent", "Let me ask you a few quick questions to personalize your loan offer...")
            st.session_state.stage = 'DISCOVER_NEEDS'
            st.rerun()
        
        # ========================================
        # STAGE: DISCOVER NEEDS
        # ========================================
        elif st.session_state.stage == 'DISCOVER_NEEDS':
            with st.chat_message("SalesAgent", avatar="💼"):
                st.write("**What do you plan to use this loan for?**")
                st.write("*(This helps us tailor the best offer for you)*")
                
                purposes = [
                    "🏠 Home Renovation",
                    "💒 Wedding Expenses",
                    "📚 Education",
                    "🏥 Medical Emergency",
                    "🚗 Vehicle Purchase",
                    "💼 Business Needs",
                    "✈️ Travel/Vacation",
                    "💳 Debt Consolidation",
                    "📱 Electronics/Gadgets",
                    "🎯 Other Personal Needs"
                ]
                
                purpose = st.selectbox("Select purpose:", purposes, key='purpose_select')
                
                if st.button("Continue ➡️"):
                    st.session_state.purpose = purpose
                    add_message("User", f"I need the loan for: {purpose}")
                    add_message("SalesAgent", f"Perfect! {purpose.split(' ', 1)[1]} is a great reason. Let's discuss the amount and terms.")
                    st.session_state.stage = 'LOAN_DETAILS'
                    st.rerun()
        
        # ========================================
        # STAGE: LOAN DETAILS
        # ========================================
        elif st.session_state.stage == 'LOAN_DETAILS':
            user_data = CRM_DB[st.session_state.user_id]
            pre_approved = OFFER_MART_API[st.session_state.user_id]
            
            with st.chat_message("SalesAgent", avatar="💼"):
                st.write("**Let's customize your loan offer:**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    loan_amount = st.number_input(
                        "💰 Loan Amount (₹)",
                        min_value=25000,
                        max_value=2000000,
                        value=min(200000, pre_approved),
                        step=25000,
                        help=f"Your pre-approved limit: ₹{pre_approved:,}",
                        key='loan_amt_input'
                    )
                    
                    if loan_amount > pre_approved:
                        st.warning(f"⚠️ Amount exceeds pre-approved limit of ₹{pre_approved:,}. Additional verification may be required.")
                
                with col2:
                    tenure = st.selectbox(
                        "📅 Loan Tenure",
                        options=[12, 24, 36, 48, 60, 72, 84],
                        format_func=lambda x: f"{x} months ({x//12} years)" if x >= 12 else f"{x} months",
                        index=2,
                        key='tenure_select'
                    )
                
                # Calculate and show EMI preview
                credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
                interest_rate = get_interest_rate(credit_score)
                emi = calculate_emi(loan_amount, interest_rate, tenure)
                total_payment = emi * tenure
                total_interest = total_payment - loan_amount
                
                st.divider()
                
                st.write("**📊 Loan Summary:**")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Monthly EMI", f"₹{emi:,.2f}")
                col2.metric("Interest Rate*", f"{interest_rate}% p.a.")
                col3.metric("Total Interest", f"₹{total_interest:,.2f}")
                
                st.caption("*Interest rate based on your credit profile")
                
                st.info(f"💡 **Total Payment:** ₹{total_payment:,.2f} over {tenure//12} years")
                
                # Check affordability
                monthly_salary = user_data['monthly_salary']
                emi_to_income_ratio = (emi / monthly_salary) * 100
                
                if emi_to_income_ratio > 50:
                    st.warning(f"⚠️ EMI is {emi_to_income_ratio:.1f}% of your monthly salary. We recommend keeping it under 50% for comfortable repayment.")
                else:
                    st.success(f"✅ EMI is {emi_to_income_ratio:.1f}% of your monthly salary - Well within comfortable limits!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("✅ Proceed with This Offer", type="primary", use_container_width=True):
                        st.session_state.loan_amount = loan_amount
                        st.session_state.loan_tenure = tenure
                        st.session_state.interest_rate = interest_rate
                        st.session_state.monthly_emi = emi
                        st.session_state.offer_accepted = True
                        
                        add_message("User", f"I'd like to proceed with ₹{loan_amount:,} for {tenure} months")
                        add_message("SalesAgent", f"Excellent choice! Your monthly EMI will be ₹{emi:,.2f} at {interest_rate}% interest rate.")
                        add_message("SalesAgent", "Let me now hand you over to our Verification team to confirm your details. This will just take a moment...")
                        add_message("MasterAgent", "🔄 Transferring to Verification Agent...")
                        
                        st.session_state.stage = 'VERIFICATION'
                        st.rerun()
                
                with col2:
                    if st.button("🔄 Modify Details", use_container_width=True):
                        st.info("Please adjust the loan amount or tenure above and click 'Proceed' when ready.")
        
        # ========================================
        # STAGE: VERIFICATION
        # ========================================
        elif st.session_state.stage == 'VERIFICATION':
            if not st.session_state.address_verified:
                time.sleep(1)
                add_message("VerificationAgent", f"Hello! I'm the Verification Agent. Let me quickly verify your details from our records. 🔍")
                
                time.sleep(1)
                with st.spinner("Fetching KYC details from CRM..."):
                    time.sleep(2)
                
                user_data = CRM_DB[st.session_state.user_id]
                
                add_message("VerificationAgent", "✅ KYC Status: **Verified**")
                add_message("VerificationAgent", f"📱 Registered Phone: {user_data['phone']}")
                add_message("VerificationAgent", f"📧 Email: {user_data['email']}")
                
                with st.chat_message("VerificationAgent", avatar="🔍"):
                    st.write(f"**🏠 Registered Address:**")
                    st.info(user_data['address'])
                    st.write("**Is this information correct?**")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("✅ Yes, All Correct", type="primary", use_container_width=True):
                            st.session_state.address_verified = True
                            add_message("User", "Yes, all details are correct ✓")
                            add_message("VerificationAgent", "Perfect! Your identity and address have been verified successfully. ✓")
                            add_message("MasterAgent", "Great! All details verified. Now connecting you to our Underwriting team for credit evaluation...")
                            add_message("MasterAgent", "🔄 Transferring to Underwriting Agent...")
                            st.session_state.stage = 'UNDERWRITING_INTRO'
                            st.rerun()
                    
                    with col2:
                        if st.button("❌ Need to Update", use_container_width=True):
                            add_message("User", "I need to update my details")
                            add_message("VerificationAgent", "No problem! Please visit your nearest branch or contact customer support at 1800-XXX-XXXX to update your details.")
                            add_message("MasterAgent", "We cannot proceed without verified details. Please update your information and return to complete your application.")
                            st.session_state.stage = 'END'
                            st.rerun()
        
        # ========================================
        # STAGE: UNDERWRITING INTRO
        # ========================================
        elif st.session_state.stage == 'UNDERWRITING_INTRO':
            time.sleep(1)
            add_message("UnderwritingAgent", "Hello! I'm the Underwriting Agent. I'll evaluate your loan application based on your credit profile and eligibility. 📊")
            time.sleep(0.5)
            add_message("UnderwritingAgent", "Let me pull your credit report and analyze your request...")
            st.session_state.stage = 'UNDERWRITING_ANALYSIS'
            st.rerun()
        
        # ========================================
        # STAGE: UNDERWRITING ANALYSIS
        # ========================================
        elif st.session_state.stage == 'UNDERWRITING_ANALYSIS':
            with st.spinner("🔍 Fetching credit report from bureau..."):
                time.sleep(2)
            
            credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
            pre_approved_limit = OFFER_MART_API[st.session_state.user_id]
            loan_amount = st.session_state.loan_amount
            user_data = CRM_DB[st.session_state.user_id]
            
            add_message("UnderwritingAgent", "✅ Credit report retrieved successfully!")
            
            with st.chat_message("UnderwritingAgent", avatar="📊"):
                st.write("**📋 Credit Analysis Report:**")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Credit Score", f"{credit_score}/900", 
                             delta="Excellent" if credit_score >= 800 else "Good" if credit_score >= 700 else "Fair")
                
                with col2:
                    st.metric("Pre-approved Limit", f"₹{pre_approved_limit:,}")
                
                with col3:
                    st.metric("Requested Amount", f"₹{loan_amount:,}")
                
                st.divider()
                
                # Show existing obligations
                if user_data['existing_loans']:
                    st.write("**📌 Existing Obligations:**")
                    for loan in user_data['existing_loans']:
                        st.write(f"- {loan}")
                else:
                    st.success("✅ No existing loans - Clean credit history!")
            
            time.sleep(1)
            add_message("UnderwritingAgent", f"Analyzing eligibility for ₹{loan_amount:,}...")
            
            with st.spinner("🔄 Running underwriting algorithms..."):
                time.sleep(2)
            
            # Decision Logic
            if loan_amount <= pre_approved_limit and credit_score >= 700:
                # Instant Approval
                st.session_state.stage = 'INSTANT_APPROVAL'
            elif pre_approved_limit < loan_amount <= 2 * pre_approved_limit and credit_score >= 700:
                # Salary slip required
                st.session_state.stage = 'SALARY_SLIP_REQUIRED'
            elif credit_score < 700:
                # Low credit score rejection
                st.session_state.stage = 'REJECTION_CREDIT'
            else:
                # Amount too high
                st.session_state.stage = 'REJECTION_AMOUNT'
            
            st.rerun()
        
        # ========================================
        # STAGE: INSTANT APPROVAL
        # ========================================
        elif st.session_state.stage == 'INSTANT_APPROVAL':
            add_message("UnderwritingAgent", "🎉 **CONGRATULATIONS!** Your loan application has been **INSTANTLY APPROVED!**")
            
            time.sleep(0.5)
            
            user_data = CRM_DB[st.session_state.user_id]
            credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
            
            with st.chat_message("UnderwritingAgent", avatar="📊"):
                st.success("✅ **LOAN APPROVED**")
                st.write("**Approval Criteria Met:**")
                st.write(f"✓ Loan amount within pre-approved limit")
                st.write(f"✓ Credit score {credit_score}/900 - Excellent standing")
                st.write(f"✓ EMI to income ratio: {(st.session_state.monthly_emi/user_data['monthly_salary']*100):.1f}% (Within limits)")
                st.write(f"✓ All KYC documents verified")
            
            time.sleep(0.5)
            add_message("MasterAgent", "Fantastic news! I'm now generating your sanction letter. Please wait...")
            add_message("MasterAgent", "🔄 Transferring to Document Generation Agent...")
            
            st.session_state.stage = 'GENERATE_LETTER'
            st.rerun()
        
        # ========================================
        # STAGE: SALARY SLIP REQUIRED
        # ========================================
        elif st.session_state.stage == 'SALARY_SLIP_REQUIRED':
            if not st.session_state.salary_slip_uploaded:
                add_message("UnderwritingAgent", "Your requested amount is higher than your pre-approved limit, but you're still eligible! 📈")
                add_message("UnderwritingAgent", "To proceed, we need to verify your income. Please upload your latest salary slip or bank statement (last 3 months).")
                
                with st.chat_message("UnderwritingAgent", avatar="📊"):
                    st.info("📄 **Document Upload Required**")
                    st.write("Please upload one of the following:")
                    st.write("• Latest salary slip (PDF/JPG/PNG)")
                    st.write("• Bank statement for last 3 months")
                    st.write("• Form 16 or ITR")
                    
                    uploaded_file = st.file_uploader(
                        "Choose file",
                        type=['pdf', 'jpg', 'jpeg', 'png'],
                        key='salary_slip'
                    )
                    
                    if uploaded_file:
                        st.success(f"✅ File uploaded: {uploaded_file.name}")
                        
                        if st.button("🔍 Verify Document", type="primary", use_container_width=True):
                            add_message("User", f"Uploaded document: {uploaded_file.name}")
                            add_message("UnderwritingAgent", "Thank you! Analyzing your salary document...")
                            
                            with st.spinner("🔄 Processing document with AI OCR..."):
                                time.sleep(2)
                            
                            with st.spinner("📊 Verifying income details..."):
                                time.sleep(2)
                            
                            user_data = CRM_DB[st.session_state.user_id]
                            salary = user_data['monthly_salary']
                            emi = st.session_state.monthly_emi
                            emi_ratio = (emi / salary) * 100
                            
                            add_message("UnderwritingAgent", f"✅ Document verified successfully!")
                            add_message("UnderwritingAgent", f"Monthly Salary Detected: ₹{salary:,}")
                            add_message("UnderwritingAgent", f"Proposed EMI: ₹{emi:,.2f} ({emi_ratio:.1f}% of salary)")
                            
                            if emi_ratio <= 50:
                                add_message("UnderwritingAgent", "✅ EMI is well within 50% limit. **Loan APPROVED!** 🎉")
                                st.session_state.salary_slip_uploaded = True
                                st.session_state.stage = 'INSTANT_APPROVAL'
                            else:
                                add_message("UnderwritingAgent", "⚠️ EMI exceeds 50% of monthly salary. Unfortunately, we cannot approve this amount.")
                                st.session_state.stage = 'REJECTION_AMOUNT'
                            
                            st.rerun()
        
        # ========================================
        # STAGE: REJECTION - CREDIT SCORE
        # ========================================
        elif st.session_state.stage == 'REJECTION_CREDIT':
            credit_score = CREDIT_BUREAU_API[st.session_state.user_id]
            pre_approved_limit = OFFER_MART_API[st.session_state.user_id]
            
            add_message("UnderwritingAgent", "After careful review of your application, I have some updates to share.")
            
            with st.chat_message("UnderwritingAgent", avatar="📊"):
                st.warning("⚠️ **Application Status: Additional Review Required**")
                st.write(f"Your credit score of **{credit_score}** is slightly below our instant approval threshold of 700.")
                st.write("However, don't worry! You still have options:")
            
            time.sleep(0.5)
            add_message("MasterAgent", f"I understand this might be disappointing. However, you're still eligible for your pre-approved amount of **₹{pre_approved_limit:,}** with special terms.")
            
            with st.chat_message("MasterAgent", avatar="🤖"):
                st.info(f"**Alternative Offer Available: ₹{pre_approved_limit:,}**")
                st.write("Benefits:")
                st.write("✓ Quick approval process")
                st.write("✓ Competitive interest rates")
                st.write("✓ Flexible repayment options")
                
                st.write("**Would you like to proceed with this offer?**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("✅ Yes, Accept Offer", type="primary", use_container_width=True):
                        st.session_state.loan_amount = pre_approved_limit
                        # Recalculate EMI
                        st.session_state.monthly_emi = calculate_emi(
                            pre_approved_limit,
                            st.session_state.interest_rate,
                            st.session_state.loan_tenure
                        )
                        
                        add_message("User", f"Yes, I'll proceed with ₹{pre_approved_limit:,}")
                        add_message("MasterAgent", "Excellent decision! Processing your revised application...")
                        st.session_state.stage = 'INSTANT_APPROVAL'
                        st.rerun()
                
                with col2:
                    if st.button("❌ No, Cancel", use_container_width=True):
                        add_message("User", "I'll cancel this application for now")
                        add_message("MasterAgent", "I understand. Feel free to reapply once you've improved your credit score. We're here to help anytime!")
                        add_message("MasterAgent", "💡 **Tip:** Regular EMI payments and credit card bill settlements can help improve your score.")
                        st.session_state.stage = 'END'
                        st.rerun()
        
        # ========================================
        # STAGE: REJECTION - AMOUNT TOO HIGH
        # ========================================
        elif st.session_state.stage == 'REJECTION_AMOUNT':
            loan_amount = st.session_state.loan_amount
            pre_approved_limit = OFFER_MART_API[st.session_state.user_id]
            
            add_message("UnderwritingAgent", "I've completed the analysis of your application.")
            
            with st.chat_message("UnderwritingAgent", avatar="📊"):
                st.warning("⚠️ **Application Status: Amount Exceeds Eligibility**")
                st.write(f"The requested amount of ₹{loan_amount:,} exceeds our lending limits based on current eligibility criteria.")
            
            time.sleep(0.5)
            add_message("MasterAgent", f"However, you're pre-approved for **₹{pre_approved_limit:,}** which we can disburse immediately!")
            
            # Calculate EMI for pre-approved amount
            revised_emi = calculate_emi(
                pre_approved_limit,
                st.session_state.interest_rate,
                st.session_state.loan_tenure
            )
            
            with st.chat_message("MasterAgent", avatar="🤖"):
                st.info(f"**Revised Offer: ₹{pre_approved_limit:,}**")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Loan Amount", f"₹{pre_approved_limit:,}")
                col2.metric("Monthly EMI", f"₹{revised_emi:,.2f}")
                col3.metric("Interest Rate", f"{st.session_state.interest_rate}%")
                
                st.write("**Would you like to proceed with this amount?**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("✅ Accept Revised Offer", type="primary", use_container_width=True):
                        st.session_state.loan_amount = pre_approved_limit
                        st.session_state.monthly_emi = revised_emi
                        
                        add_message("User", f"Yes, I'll proceed with ₹{pre_approved_limit:,}")
                        add_message("MasterAgent", "Great! Processing your application now...")
                        st.session_state.stage = 'INSTANT_APPROVAL'
                        st.rerun()
                
                with col2:
                    if st.button("❌ Decline Offer", use_container_width=True):
                        add_message("User", "No, thank you. I'll explore other options.")
                        add_message("MasterAgent", "Thank you for considering Tata Capital. You can reapply after 6 months for a higher limit!")
                        add_message("MasterAgent", "💡 **Build your relationship:** Maintain good credit history and consider our other products to increase your eligibility.")
                        st.session_state.stage = 'END'
                        st.rerun()
        
        # ========================================
        # STAGE: GENERATE SANCTION LETTER
        # ========================================
        elif st.session_state.stage == 'GENERATE_LETTER':
            time.sleep(1)
            add_message("SanctionLetterGenerator", "Initiating sanction letter generation process... 📄")
            
            with st.spinner("📝 Generating sanction letter..."):
                time.sleep(2)
            
            user_data = CRM_DB[st.session_state.user_id]
            
            # Generate sanction letter details
            loan_id = f"TC{st.session_state.user_id[4:]}{random.randint(1000, 9999)}"
            sanction_date = datetime.now().strftime("%d-%b-%Y")
            disbursement_date = (datetime.now() + timedelta(days=2)).strftime("%d-%b-%Y")
            
            add_message("SanctionLetterGenerator", "✅ Sanction letter generated successfully!")
            
            with st.chat_message("SanctionLetterGenerator", avatar="📄"):
                st.success("🎉 **LOAN SANCTION LETTER**")
                
                st.markdown(f"""
                ---
                **TATA CAPITAL FINANCIAL SERVICES LTD.**  
                *Personal Loan Sanction Letter*
                
                **Date:** {sanction_date}  
                **Loan ID:** {loan_id}
                
                **Dear {user_data['name']},**
                
                Congratulations! We are pleased to inform you that your personal loan application has been **approved**.
                
                **Loan Details:**
                
                | Particulars | Details |
                |-------------|---------|
                | **Loan Amount** | ₹{st.session_state.loan_amount:,} |
                | **Interest Rate** | {st.session_state.interest_rate}% p.a. (Reducing Balance) |
                | **Loan Tenure** | {st.session_state.loan_tenure} months ({st.session_state.loan_tenure//12} years) |
                | **Monthly EMI** | ₹{st.session_state.monthly_emi:,.2f} |
                | **Processing Fee** | ₹{int(st.session_state.loan_amount * 0.02):,} (2% of loan amount) |
                | **Expected Disbursement** | {disbursement_date} |
                
                **Purpose:** {st.session_state.purpose}
                
                **Total Amount Payable:** ₹{(st.session_state.monthly_emi * st.session_state.loan_tenure):,.2f}
                
                **Next Steps:**
                1. Sign the loan agreement (digital signature)
                2. Complete final documentation
                3. Funds will be disbursed to your registered bank account
                
                **Terms & Conditions:**
                - Prepayment allowed after 6 months with minimal charges
                - Auto-debit facility mandatory
                - Default in payment may affect credit score
                
                For any queries, contact: **1800-209-7800**
                
                **Yours sincerely,**  
                *Tata Capital Financial Services*
                
                ---
                """)
                
                st.download_button(
                    label="📥 Download Sanction Letter (PDF)",
                    data=f"Sanction Letter - {loan_id}.pdf",
                    file_name=f"Sanction_Letter_{loan_id}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
            
            time.sleep(0.5)
            add_message("MasterAgent", "🎊 Congratulations! Your loan has been approved and your sanction letter is ready!")
            add_message("MasterAgent", "Our team will contact you within 24 hours for final documentation. The loan amount will be disbursed within 2 working days.")
            
            with st.chat_message("MasterAgent", avatar="🤖"):
                st.balloons()
                
                st.write("**What would you like to do next?**")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("📧 Email Letter", use_container_width=True):
                        st.success(f"✅ Sanction letter sent to {user_data['email']}")
                
                with col2:
                    if st.button("💬 Chat Support", use_container_width=True):
                        st.info("📞 Our team will call you shortly!")
                
                with col3:
                    if st.button("🔄 New Application", use_container_width=True):
                        for key in list(st.session_state.keys()):
                            del st.session_state[key]
                        st.rerun()
            
            st.session_state.stage = 'END'
        
        # ========================================
        # STAGE: END
        # ========================================
        elif st.session_state.stage == 'END':
            with st.chat_message("MasterAgent", avatar="🤖"):
                st.write("**Thank you for choosing Tata Capital!** 🙏")
                st.write("---")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Need Help?**")
                    st.write("📞 Call: 1800-209-7800")
                    st.write("📧 Email: support@tatacapital.com")
                    st.write("🌐 Visit: www.tatacapital.com")
                
                with col2:
                    st.write("**Quick Links:**")
                    st.write("• Track Application Status")
                    st.write("• Calculate EMI")
                    st.write("• Customer Portal Login")
                
                st.write("---")
                
                if st.button("🏠 Return to Home", type="primary", use_container_width=True):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.rerun()
    
    # Footer
    st.divider()
    st.caption("🔒 Powered by Agentic AI | Tata Capital © 2024 | Secure & Confidential")
    st.caption("⚡ Prototype Demo - For Hackathon Submission")

if __name__ == "__main__":
    main()