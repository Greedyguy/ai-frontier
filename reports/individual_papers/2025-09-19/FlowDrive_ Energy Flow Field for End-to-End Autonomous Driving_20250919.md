---
keywords:
  - Autonomous Driving
  - Diffusion Models
  - Bird's Eye View Representations
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14303
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:43:43.716827",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Autonomous Driving",
    "Diffusion Models",
    "Bird's Eye View Representations"
  ],
  "rejected_keywords": [
    "Energy Flow Fields"
  ],
  "similarity_scores": {
    "Autonomous Driving": 0.78,
    "Diffusion Models": 0.75,
    "Bird's Eye View Representations": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# FlowDrive: Energy Flow Field for End-to-End Autonomous Driving

**Korean Title:** FlowDrive: 자율주행을 위한 종단 간 에너지 흐름 필드

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Autonomous Driving|end-to-end autonomous driving]], [[keywords/Diffusion Models|conditional diffusion planner]]
**⚡ Unique Technical**: [[keywords/Bird's Eye View Representations|BEV representations]]

## 🔗 유사한 논문
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (85.1% similar)
- [[Disturbance-Aware_Dynamical_Trajectory_Planning_for_Air-Land_Bimodal_Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (81.0% similar)
- [[FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (80.7% similar)
- [[VEGA Electric Vehicle Navigation Agent via Physics-Informed Neural Operator and Proximal Policy Optimization]] (80.2% similar)
- [[FlowAct A Proactive Multimodal Human-robot Interaction System with Continuous Flow of Perception and Modular Action Sub-systems]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14303v1 Announce Type: cross 
Abstract: Recent advances in end-to-end autonomous driving leverage multi-view images to construct BEV representations for motion planning. In motion planning, autonomous vehicles need considering both hard constraints imposed by geometrically occupied obstacles (e.g., vehicles, pedestrians) and soft, rule-based semantics with no explicit geometry (e.g., lane boundaries, traffic priors). However, existing end-to-end frameworks typically rely on BEV features learned in an implicit manner, lacking explicit modeling of risk and guidance priors for safe and interpretable planning. To address this, we propose FlowDrive, a novel framework that introduces physically interpretable energy-based flow fields-including risk potential and lane attraction fields-to encode semantic priors and safety cues into the BEV space. These flow-aware features enable adaptive refinement of anchor trajectories and serve as interpretable guidance for trajectory generation. Moreover, FlowDrive decouples motion intent prediction from trajectory denoising via a conditional diffusion planner with feature-level gating, alleviating task interference and enhancing multimodal diversity. Experiments on the NAVSIM v2 benchmark demonstrate that FlowDrive achieves state-of-the-art performance with an EPDMS of 86.3, surpassing prior baselines in both safety and planning quality. The project is available at https://astrixdrive.github.io/FlowDrive.github.io/.

## 🔍 Abstract (한글 번역)

arXiv:2509.14303v1 발표 유형: 교차  
초록: 최근의 종단 간 자율 주행 발전은 다중 시야 이미지를 활용하여 모션 플래닝을 위한 BEV 표현을 구축합니다. 모션 플래닝에서 자율 주행 차량은 기하학적으로 점유된 장애물(예: 차량, 보행자)에 의해 부과된 강한 제약 조건과 명시적인 기하학이 없는 규칙 기반의 의미론적 요소(예: 차선 경계, 교통 우선권)를 모두 고려해야 합니다. 그러나 기존의 종단 간 프레임워크는 일반적으로 암시적인 방식으로 학습된 BEV 특징에 의존하여 안전하고 해석 가능한 계획을 위한 위험 및 안내 우선권의 명시적 모델링이 부족합니다. 이를 해결하기 위해 우리는 FlowDrive라는 새로운 프레임워크를 제안합니다. 이는 의미론적 우선권과 안전 신호를 BEV 공간에 인코딩하기 위해 위험 잠재력 및 차선 매력 필드를 포함한 물리적으로 해석 가능한 에너지 기반 흐름 필드를 도입합니다. 이러한 흐름 인식 특징은 앵커 궤적의 적응적 세련화를 가능하게 하고 궤적 생성에 대한 해석 가능한 지침으로 작용합니다. 더욱이, FlowDrive는 특징 수준 게이팅을 갖춘 조건부 확산 플래너를 통해 궤적 노이즈 제거에서 모션 의도 예측을 분리하여 작업 간섭을 완화하고 다중 모드 다양성을 향상시킵니다. NAVSIM v2 벤치마크 실험에서 FlowDrive는 86.3의 EPDMS로 최첨단 성능을 달성하여 안전성과 계획 품질 모두에서 이전 기준선을 능가합니다. 프로젝트는 https://astrixdrive.github.io/FlowDrive.github.io/에서 확인할 수 있습니다.

## 📝 요약

FlowDrive는 자율주행 차량의 안전하고 해석 가능한 경로 계획을 위해 새로운 에너지 기반 흐름 필드를 도입한 프레임워크입니다. 이 프레임워크는 위험 잠재력과 차선 매력 필드를 통해 BEV 공간에 의미론적 우선순위와 안전 신호를 명시적으로 인코딩합니다. 이를 통해 앵커 경로의 적응적 세부 조정과 경로 생성에 대한 해석 가능한 지침을 제공합니다. 또한, FlowDrive는 조건부 확산 계획자를 사용하여 모션 의도 예측과 경로 잡음 제거를 분리하여 작업 간섭을 줄이고 다중 모드 다양성을 향상시킵니다. NAVSIM v2 벤치마크 실험에서 FlowDrive는 86.3의 EPDMS로 기존의 기준을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FlowDrive는 에너지 기반 흐름장을 도입하여 BEV 공간에 의미론적 우선순위와 안전 신호를 인코딩합니다.

- 2. 이 프레임워크는 리스크 잠재력과 차선 매력장을 포함하여 물리적으로 해석 가능한 흐름장을 사용합니다.

- 3. FlowDrive는 조건부 확산 계획자를 통해 모션 의도 예측과 경로 노이즈 제거를 분리하여 작업 간섭을 줄이고 다중 모드 다양성을 향상시킵니다.

- 4. NAVSIM v2 벤치마크 실험에서 FlowDrive는 EPDMS 86.3을 기록하며 안전성과 계획 품질에서 기존 기준을 능가하는 성과를 보였습니다.

---

*Generated on 2025-09-19 14:54:02*