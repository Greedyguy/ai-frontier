# GUI-ARP: Enhancing Grounding with Adaptive Region Perception for GUI Agents

**Korean Title:** GUI-ARP: GUI 에이전트를 위한 적응형 영역 인식을 통한 그라운딩 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Multi-stage Inference

## 🔗 유사한 논문
- [[2025-09-18/InfraMind_ A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management_20250918|InfraMind A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management]] (81.4% similar)
- [[2025-09-19/GAF_ Gaussian Action Field as a Dynamic World Model for Robotic Manipulation_20250919|GAF Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (81.1% similar)
- [[2025-09-19/ScaleCUA_ Scaling Open-Source Computer Use Agents with Cross-Platform Data_20250919|ScaleCUA Scaling Open-Source Computer Use Agents with Cross-Platform Data]] (80.8% similar)
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (80.2% similar)
- [[2025-09-18/See, Think, Act_ Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles_20250918|See, Think, Act Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15532v1 Announce Type: cross 
Abstract: Existing GUI grounding methods often struggle with fine-grained localization in high-resolution screenshots. To address this, we propose GUI-ARP, a novel framework that enables adaptive multi-stage inference. Equipped with the proposed Adaptive Region Perception (ARP) and Adaptive Stage Controlling (ASC), GUI-ARP dynamically exploits visual attention for cropping task-relevant regions and adapts its inference strategy, performing a single-stage inference for simple cases and a multi-stage analysis for more complex scenarios. This is achieved through a two-phase training pipeline that integrates supervised fine-tuning with reinforcement fine-tuning based on Group Relative Policy Optimization (GRPO). Extensive experiments demonstrate that the proposed GUI-ARP achieves state-of-the-art performance on challenging GUI grounding benchmarks, with a 7B model reaching 60.8% accuracy on ScreenSpot-Pro and 30.9% on UI-Vision benchmark. Notably, GUI-ARP-7B demonstrates strong competitiveness against open-source 72B models (UI-TARS-72B at 38.1%) and proprietary models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15532v1 발표 유형: 교차  
초록: 기존의 GUI 그라운딩 방법은 고해상도 스크린샷에서 세밀한 위치 지정에 어려움을 겪는 경우가 많습니다. 이를 해결하기 위해, 우리는 적응형 다단계 추론을 가능하게 하는 새로운 프레임워크인 GUI-ARP를 제안합니다. 제안된 적응형 영역 인식(ARP)과 적응형 단계 제어(ASC)를 갖춘 GUI-ARP는 시각적 주의를 동적으로 활용하여 작업 관련 영역을 자르고, 간단한 경우에는 단일 단계 추론을 수행하고 복잡한 시나리오에서는 다단계 분석을 수행하는 추론 전략을 조정합니다. 이는 그룹 상대 정책 최적화(GRPO)를 기반으로 한 강화 미세 조정과 감독 미세 조정을 통합한 2단계 훈련 파이프라인을 통해 달성됩니다. 광범위한 실험을 통해 제안된 GUI-ARP가 도전적인 GUI 그라운딩 벤치마크에서 최첨단 성능을 달성했음을 보여주며, 7B 모델이 ScreenSpot-Pro에서 60.8%의 정확도와 UI-Vision 벤치마크에서 30.9%를 기록했습니다. 특히, GUI-ARP-7B는 오픈 소스 72B 모델(UI-TARS-72B의 38.1%) 및 독점 모델에 대해 강력한 경쟁력을 보여줍니다.

## 📝 요약

기존의 GUI 그라운딩 방법은 고해상도 스크린샷에서 세밀한 위치 지정에 어려움을 겪습니다. 이를 해결하기 위해, 우리는 GUI-ARP라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 적응형 다단계 추론을 가능하게 하며, Adaptive Region Perception (ARP)과 Adaptive Stage Controlling (ASC)을 통해 시각적 주의를 활용하여 관련 영역을 자르고, 간단한 경우에는 단일 단계 추론을, 복잡한 경우에는 다단계 분석을 수행합니다. 두 단계의 훈련 파이프라인을 통해 감독 학습과 강화 학습을 통합하여 이 목표를 달성합니다. 실험 결과, GUI-ARP는 ScreenSpot-Pro에서 60.8%, UI-Vision 벤치마크에서 30.9%의 정확도를 기록하며, 최첨단 성능을 보여주었습니다. 특히, GUI-ARP-7B는 72B 모델과 비교해도 경쟁력을 나타냅니다.

## 🎯 주요 포인트

- 1. GUI-ARP는 고해상도 스크린샷에서 세밀한 위치 지정 문제를 해결하기 위해 적응형 다단계 추론을 가능하게 하는 새로운 프레임워크입니다.

- 2. Adaptive Region Perception (ARP)와 Adaptive Stage Controlling (ASC)를 통해 시각적 주의를 활용하여 관련 영역을 자르고, 간단한 경우에는 단일 단계 추론을, 복잡한 경우에는 다단계 분석을 수행합니다.

- 3. GUI-ARP는 감독된 미세 조정과 Group Relative Policy Optimization (GRPO)에 기반한 강화 미세 조정을 통합한 두 단계의 훈련 파이프라인을 통해 구현됩니다.

- 4. 실험 결과, GUI-ARP는 ScreenSpot-Pro에서 60.8%, UI-Vision 벤치마크에서 30.9%의 정확도를 기록하며 최첨단 성능을 달성했습니다.

- 5. GUI-ARP-7B는 오픈소스 72B 모델 및 독점 모델과 비교하여 강력한 경쟁력을 보여줍니다.

---

*Generated on 2025-09-22 14:01:00*