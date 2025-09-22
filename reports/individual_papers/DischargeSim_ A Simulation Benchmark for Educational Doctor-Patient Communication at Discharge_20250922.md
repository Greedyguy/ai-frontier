# DischargeSim: A Simulation Benchmark for Educational Doctor-Patient Communication at Discharge

**Korean Title:** 퇴원 시 의사-환자 커뮤니케이션 교육을 위한 시뮬레이션 벤치마크: DischargeSim

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized Discharge Education

## 🔗 유사한 논문
- [[2025-09-18/When Avatars Have Personality_ Effects on Engagement and Communication in Immersive Medical Training_20250918|When Avatars Have Personality Effects on Engagement and Communication in Immersive Medical Training]] (83.2% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (82.2% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (81.9% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (81.6% similar)
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era A Survey]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07188v3 Announce Type: replace-cross 
Abstract: Discharge communication is a critical yet underexplored component of patient care, where the goal shifts from diagnosis to education. While recent large language model (LLM) benchmarks emphasize in-visit diagnostic reasoning, they fail to evaluate models' ability to support patients after the visit. We introduce DischargeSim, a novel benchmark that evaluates LLMs on their ability to act as personalized discharge educators. DischargeSim simulates post-visit, multi-turn conversations between LLM-driven DoctorAgents and PatientAgents with diverse psychosocial profiles (e.g., health literacy, education, emotion). Interactions are structured across six clinically grounded discharge topics and assessed along three axes: (1) dialogue quality via automatic and LLM-as-judge evaluation, (2) personalized document generation including free-text summaries and structured AHRQ checklists, and (3) patient comprehension through a downstream multiple-choice exam. Experiments across 18 LLMs reveal significant gaps in discharge education capability, with performance varying widely across patient profiles. Notably, model size does not always yield better education outcomes, highlighting trade-offs in strategy use and content prioritization. DischargeSim offers a first step toward benchmarking LLMs in post-visit clinical education and promoting equitable, personalized patient support.

## 🔍 Abstract (한글 번역)

arXiv:2509.07188v3 발표 유형: 교차 교체  
초록: 퇴원 소통은 진단에서 교육으로 목표가 전환되는 환자 관리의 중요한 요소이지만, 충분히 탐구되지 않은 분야입니다. 최근 대형 언어 모델(LLM) 벤치마크는 방문 중 진단 추론을 강조하지만, 방문 후 환자를 지원하는 모델의 능력을 평가하지 못합니다. 우리는 LLM이 개인화된 퇴원 교육자로서의 능력을 평가하는 새로운 벤치마크인 DischargeSim을 소개합니다. DischargeSim은 다양한 심리사회적 프로파일(예: 건강 문해력, 교육, 감정)을 가진 PatientAgent와 LLM 기반 DoctorAgent 간의 방문 후 다중 턴 대화를 시뮬레이션합니다. 상호작용은 임상적으로 기반이 있는 여섯 가지 퇴원 주제를 중심으로 구조화되며, 세 가지 축을 따라 평가됩니다: (1) 자동 및 LLM-판사 평가를 통한 대화 품질, (2) 자유 텍스트 요약 및 구조화된 AHRQ 체크리스트를 포함한 개인화된 문서 생성, (3) 후속 다지선다형 시험을 통한 환자 이해도. 18개의 LLM에 대한 실험은 퇴원 교육 능력에서 상당한 격차를 드러내며, 환자 프로파일에 따라 성과가 크게 달라짐을 보여줍니다. 특히 모델 크기가 항상 더 나은 교육 결과를 가져오지는 않으며, 전략 사용 및 콘텐츠 우선순위 설정에서의 절충점을 강조합니다. DischargeSim은 방문 후 임상 교육에서 LLM을 벤치마킹하고 공평하고 개인화된 환자 지원을 촉진하기 위한 첫걸음을 제공합니다.

## 📝 요약

이 논문은 환자 퇴원 후 교육을 지원하는 대형 언어 모델(LLM)의 능력을 평가하기 위해 DischargeSim이라는 새로운 벤치마크를 소개합니다. DischargeSim은 다양한 사회심리적 프로필을 가진 환자와 LLM 기반 의사 에이전트 간의 대화를 시뮬레이션하여 모델의 교육적 역할을 평가합니다. 이 벤치마크는 대화의 질, 개인화된 문서 생성, 환자 이해도를 평가하며, 18개의 LLM 실험 결과, 모델 크기가 항상 더 나은 교육 결과를 보장하지 않음을 발견했습니다. DischargeSim은 퇴원 후 임상 교육에서 LLM의 성능을 평가하고 개인화된 환자 지원을 촉진하는 첫 걸음을 제시합니다.

## 🎯 주요 포인트

- 1. DischargeSim은 LLM을 개인화된 퇴원 교육자로 평가하는 새로운 벤치마크로, 환자 방문 후의 대화 능력을 측정합니다.

- 2. 이 벤치마크는 다양한 심리사회적 프로필을 가진 환자들과의 다중 턴 대화를 시뮬레이션하여 LLM의 교육 능력을 평가합니다.

- 3. 실험 결과, 모델 크기가 항상 더 나은 교육 결과를 보장하지 않으며, 전략 사용과 콘텐츠 우선순위 설정에서의 절충이 필요함을 보여줍니다.

- 4. DischargeSim은 LLM의 퇴원 후 임상 교육을 평가하고, 공정하고 개인화된 환자 지원을 촉진하기 위한 첫걸음을 제공합니다.

---

*Generated on 2025-09-22 15:02:47*