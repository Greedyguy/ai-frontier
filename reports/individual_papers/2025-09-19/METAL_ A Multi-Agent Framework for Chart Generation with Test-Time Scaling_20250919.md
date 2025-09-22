
# METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling

**Korean Title:** METAL: 테스트 시점 확장 기능을 갖춘 차트 생성용 다중 에이전트 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi Agent Framework

## 🔗 유사한 논문
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (78.9% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (78.7% similar)
- [[AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (78.6% similar)
- [[Towards_Robust_Agentic_CUDA_Kernel_Benchmarking,_Verification,_and_Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.5% similar)
- [[TableDART Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.17651v4 Announce Type: replace-cross 
Abstract: Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and healthcare. In this work, we build a vision-language model (VLM) based multi-agent framework for effective automatic chart generation. Generating high-quality charts requires both strong visual design skills and precise coding capabilities that embed the desired visual properties into code. Such a complex multi-modal reasoning process is difficult for direct prompting of VLMs. To resolve these challenges, we propose METAL, a multi-agent framework that decomposes the task of chart generation into the iterative collaboration among specialized agents. METAL achieves 5.2% improvement over the current best result in the chart generation task. The METAL framework exhibits the phenomenon of test-time scaling: its performance increases monotonically as the logarithmic computational budget grows from 512 to 8192 tokens. In addition, we find that separating different modalities during the critique process of METAL boosts the self-correction capability of VLMs in the multimodal context.

## 🔍 Abstract (한글 번역)

arXiv:2502.17651v4 발표 유형: 교차 교체  
초록: 차트 생성은 텍스트, 레이아웃, 색상 및 유형과 같은 원하는 시각적 속성을 충족하는 차트를 생성하기 위한 코드를 생성하는 것을 목표로 합니다. 이는 금융 분석, 연구 발표, 교육 및 의료 분야에서 자동 전문 보고서 생성을 가능하게 하는 큰 잠재력을 가지고 있습니다. 본 연구에서는 효과적인 자동 차트 생성을 위한 비전-언어 모델(VLM) 기반의 다중 에이전트 프레임워크를 구축합니다. 고품질의 차트를 생성하려면 강력한 시각적 디자인 기술과 원하는 시각적 속성을 코드에 포함시키는 정밀한 코딩 능력이 필요합니다. 이러한 복잡한 다중 모달 추론 과정은 VLM을 직접적으로 프롬프트하는 데 어려움이 있습니다. 이러한 문제를 해결하기 위해, 우리는 차트 생성 작업을 전문화된 에이전트 간의 반복적인 협업으로 분해하는 다중 에이전트 프레임워크인 METAL을 제안합니다. METAL은 차트 생성 작업에서 현재 최고의 결과보다 5.2%의 개선을 달성합니다. METAL 프레임워크는 테스트 시간 확장의 현상을 보여줍니다: 성능은 512에서 8192 토큰으로 로그 규모의 계산 예산이 증가함에 따라 단조롭게 증가합니다. 또한, METAL의 비판 과정에서 서로 다른 모달리티를 분리하는 것이 다중 모달 컨텍스트에서 VLM의 자기 수정 능력을 향상시킨다는 것을 발견했습니다.

## 📝 요약

이 논문은 차트 생성 자동화를 위한 비전-언어 모델(VLM) 기반의 다중 에이전트 프레임워크인 METAL을 제안합니다. 차트 생성은 시각적 디자인과 코드 작성 능력이 모두 요구되는 복잡한 작업으로, METAL은 이를 전문화된 에이전트 간의 협업을 통해 해결합니다. METAL은 기존 최고 성능 대비 5.2% 향상을 보였으며, 테스트 시 계산 자원이 증가할수록 성능이 향상되는 특성을 나타냅니다. 또한, 다양한 모달리티를 분리하여 비판 과정을 수행하면 VLM의 자기 수정 능력이 향상됨을 발견했습니다. 이 연구는 금융 분석, 연구 발표, 교육, 의료 분야의 자동 보고서 생성에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 차트 생성은 금융 분석, 연구 발표, 교육 및 의료 분야에서 자동화된 전문 보고서 생성을 가능하게 하는 잠재력을 가지고 있습니다.

- 2. METAL은 차트 생성 작업을 전문 에이전트 간의 반복적인 협업으로 분해하는 다중 에이전트 프레임워크를 제안합니다.

- 3. METAL 프레임워크는 차트 생성 작업에서 현재 최고 결과보다 5.2% 향상된 성능을 달성했습니다.

- 4. METAL의 테스트 시간 확장 현상은 계산 예산이 512에서 8192 토큰으로 증가함에 따라 성능이 단조롭게 증가하는 것을 보여줍니다.

- 5. METAL의 비평 과정에서 서로 다른 모달리티를 분리하는 것이 다중 모달 컨텍스트에서 VLM의 자기 수정 능력을 향상시킵니다.

---

*Generated on 2025-09-19 15:11:50*