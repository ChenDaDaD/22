import streamlit as st

def main():
    st.set_page_config(
        page_title="健康指标评估系统",
        page_icon="🩺",
        layout="centered"
    )

    # 自定义样式
    st.markdown("""
    <style>
    .normal { color: #28a745; }
    .warning { color: #ffc107; font-weight: bold; }
    .danger { color: #dc3545; }
    .section { padding: 15px; border-radius: 10px; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

    st.title("健康指标评估系统")
    
    with st.form("health_form"):
        # 基本信息
        st.header("基本信息")
        col1, col2 = st.columns(2)
        gender = col1.radio("性别", ["男", "女"])
        age = col2.number_input("年龄", 1, 120, 30)
        
        # 身体指标
        st.header("身体测量")
        col1, col2 = st.columns(2)
        height = col1.number_input("身高 (cm)", 50.0, 250.0, 170.0)
        weight = col2.number_input("体重 (kg)", 20.0, 200.0, 65.0)
        waist = st.number_input("腰围 (cm)", 50.0, 200.0, 80.0)
        
        # 血压输入
        st.header("血压测量")
        col1, col2 = st.columns(2)
        systolic = col1.number_input("收缩压 (mmHg)", 50, 250, 120)
        diastolic = col2.number_input("舒张压 (mmHg)", 30, 150, 80)
        
        # 生化指标
        st.header("生化指标")
        col1, col2 = st.columns(2)
        glucose = col1.number_input("空腹血糖 (mmol/L)", 2.0, 30.0, 5.0)
        bilirubin = col2.number_input("总胆红素 (μmol/L)", 1.0, 100.0, 12.0)
        
        # 病史信息
        st.header("病史信息")
        has_diabetes = st.checkbox("确诊糖尿病")
        
        submitted = st.form_submit_button("生成评估报告")

    if submitted:
        generate_report(gender, age, height, weight, waist,
                      systolic, diastolic, glucose, bilirubin, has_diabetes)

def generate_report(gender, age, height, weight, waist,
                  systolic, diastolic, glucose, bilirubin, has_diabetes):
    st.header("健康评估报告")
    
    # 计算BMI
    bmi = weight / ((height/100)**2)
    
    # 血压评估
    st.markdown('<div class="section" style="background-color:#e9f5fe;">', unsafe_allow_html=True)
    st.subheader("血压评估")
    bp_status = ""
    if systolic < 120 and diastolic < 80:
        st.markdown(f'<p class="normal">✅ 血压正常 ({systolic}/{diastolic} mmHg)</p>', unsafe_allow_html=True)
    elif 120 <= systolic <= 129 and diastolic < 80:
        st.markdown(f'<p class="warning">⚠️ 高血压前期 ({systolic}/{diastolic} mmHg)</p>', unsafe_allow_html=True)
        bp_status = "高血压前期"
    else:
        st.markdown(f'<p class="danger">⛔ 高血压 ({systolic}/{diastolic} mmHg)</p>', unsafe_allow_html=True)
        bp_status = "高血压"
    st.markdown('</div>', unsafe_allow_html=True)

    # BMI和腰围评估
    st.markdown('<div class="section" style="background-color:#f0f9eb;">', unsafe_allow_html=True)
    st.subheader("体型评估")
    
    # BMI评估
    bmi_status = ""
    if bmi < 18.5:
        st.markdown(f'<p class="danger">⛔ BMI过低 ({bmi:.1f})</p>', unsafe_allow_html=True)
        bmi_status = "过低"
    elif 18.5 <= bmi < 24:
        st.markdown(f'<p class="normal">✅ BMI正常 ({bmi:.1f})</p>', unsafe_allow_html=True)
    elif 24 <= bmi < 28:
        st.markdown(f'<p class="warning">⚠️ 超重 ({bmi:.1f})</p>', unsafe_allow_html=True)
        bmi_status = "超重"
    else:
        st.markdown(f'<p class="danger">⛔ 肥胖 ({bmi:.1f})</p>', unsafe_allow_html=True)
        bmi_status = "肥胖"
    
    # 腰围评估
    waist_status = ""
    if (gender == "男" and waist >= 90) or (gender == "女" and waist >= 85):
        st.markdown(f'<p class="danger">⛔ 中心性肥胖 (腰围 {waist}cm)</p>', unsafe_allow_html=True)
        waist_status = "中心性肥胖"
    else:
        st.markdown(f'<p class="normal">✅ 腰围正常 ({waist}cm)</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 生化指标评估
    st.markdown('<div class="section" style="background-color:#fef7ec;">', unsafe_allow_html=True)
    st.subheader("生化指标分析")
    
    # 血糖评估
    glucose_status = ""
    if has_diabetes:
        if glucose > 7.0:
            st.markdown(f'<p class="danger">⛔ 血糖控制不佳 ({glucose} mmol/L)</p>', unsafe_allow_html=True)
            glucose_status = "控制不佳"
        else:
            st.markdown(f'<p class="normal">✅ 血糖控制良好 ({glucose} mmol/L)</p>', unsafe_allow_html=True)
    else:
        if glucose >= 7.0:
            st.markdown(f'<p class="danger">⛔ 空腹血糖升高 ({glucose} mmol/L)</p>', unsafe_allow_html=True)
            glucose_status = "升高"
        elif 6.1 <= glucose < 7.0:
            st.markdown(f'<p class="warning">⚠️ 空腹血糖受损 ({glucose} mmol/L)</p>', unsafe_allow_html=True)
            glucose_status = "受损"
        else:
            st.markdown(f'<p class="normal">✅ 血糖正常 ({glucose} mmol/L)</p>', unsafe_allow_html=True)
    
    # 胆红素评估
    bilirubin_status = ""
    if bilirubin > 20.5:
        st.markdown(f'<p class="warning">⚠️ 总胆红素升高 ({bilirubin} μmol/L)</p>', unsafe_allow_html=True)
        bilirubin_status = "升高"
    else:
        st.markdown(f'<p class="normal">✅ 总胆红素正常 ({bilirubin} μmol/L)</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 综合建议
    st.header("个性化建议")
    
    # 血压建议
    if bp_status:
        st.markdown(f"### 血压管理建议")
        if bp_status == "高血压前期":
            st.markdown("""
            - 限制钠盐摄入（每日<5g）
            - 每周进行3-5次中等强度运动
            - 每月监测血压变化
            """)
        elif bp_status == "高血压":
            st.markdown("""
            - 建议心内科就诊
            - 每日早晚测量并记录血压
            - 严格限制饮酒
            """)
    
    # 体重管理建议
    if bmi_status in ["超重", "肥胖"] or waist_status == "中心性肥胖":
        st.markdown(f"### 体重管理建议")
        advice = []
        if waist_status == "中心性肥胖":
            advice.append("- 重点进行腰围管理，目标每月减少1-2cm")
        if bmi_status == "超重":
            advice.append("- 建议3个月内减重3-5%")
        elif bmi_status == "肥胖":
            advice.append("- 建议6个月内减重5-10%")
        advice.append("- 增加膳食纤维摄入（每日25-30g）")
        advice.append("- 每周至少150分钟有氧运动")
        for item in advice:
            st.markdown(item)
    
    # 血糖建议
    if glucose_status in ["控制不佳", "升高", "受损"]:
        st.markdown(f"### 血糖管理建议")
        if has_diabetes:
            st.markdown("""
            - 每日监测空腹及餐后2小时血糖
            - 每3个月检查糖化血红蛋白
            - 注意足部护理和眼部检查
            """)
        else:
            st.markdown("""
            - 建议进行OGTT糖耐量试验
            - 减少精制碳水化合物的摄入
            - 增加全谷物和膳食纤维
            """)
    
    # 总胆红素建议
    if bilirubin_status == "升高":
        st.markdown(f"### 肝胆健康建议")
        st.markdown("""
        - 建议检查肝功能全套
        - 避免饮酒和肝毒性药物
        - 保证充足睡眠（每日7-8小时）
        """)

if __name__ == "__main__":
    main()