
# RationAnomaly: Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning

**Korean Title:** RationAnomaly: 사고의 연쇄와 강화 학습을 통한 합리성 기반 로그 이상 탐지

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Reinforcement Learning

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14693v1 Announce Type: new 
Abstract: Logs constitute a form of evidence signaling the operational status of software systems. Automated log anomaly detection is crucial for ensuring the reliability of modern software systems. However, existing approaches face significant limitations: traditional deep learning models lack interpretability and generalization, while methods leveraging Large Language Models are often hindered by unreliability and factual inaccuracies. To address these issues, we propose RationAnomaly, a novel framework that enhances log anomaly detection by synergizing Chain-of-Thought (CoT) fine-tuning with reinforcement learning. Our approach first instills expert-like reasoning patterns using CoT-guided supervised fine-tuning, grounded in a high-quality dataset corrected through a rigorous expert-driven process. Subsequently, a reinforcement learning phase with a multi-faceted reward function optimizes for accuracy and logical consistency, effectively mitigating hallucinations. Experimentally, RationAnomaly outperforms state-of-the-art baselines, achieving superior F1-scores on key benchmarks while providing transparent, step-by-step analytical outputs. We have released the corresponding resources, including code and datasets.

## 🔍 Abstract (한글 번역)

arXiv:2509.14693v1 발표 유형: 신규  
초록: 로그는 소프트웨어 시스템의 운영 상태를 나타내는 증거의 한 형태입니다. 자동화된 로그 이상 탐지는 현대 소프트웨어 시스템의 신뢰성을 보장하는 데 필수적입니다. 그러나 기존 접근 방식에는 중요한 한계가 있습니다. 전통적인 딥러닝 모델은 해석 가능성과 일반화 능력이 부족하고, 대형 언어 모델을 활용하는 방법은 종종 신뢰성과 사실적 정확성에 의해 저해됩니다. 이러한 문제를 해결하기 위해, 우리는 Chain-of-Thought (CoT) 미세 조정과 강화 학습을 결합하여 로그 이상 탐지를 향상시키는 새로운 프레임워크인 RationAnomaly를 제안합니다. 우리의 접근 방식은 먼저 전문가와 같은 추론 패턴을 CoT 기반의 감독된 미세 조정을 통해 주입하며, 이는 엄격한 전문가 주도 프로세스를 통해 수정된 고품질 데이터셋에 기반합니다. 그 후, 다면적인 보상 함수를 가진 강화 학습 단계가 정확성과 논리적 일관성을 최적화하여 환각을 효과적으로 완화합니다. 실험적으로, RationAnomaly는 주요 벤치마크에서 뛰어난 F1 점수를 달성하며, 투명하고 단계별 분석 출력을 제공하면서 최첨단 기준을 능가합니다. 우리는 코드와 데이터셋을 포함한 관련 자원을 공개했습니다.

## 📝 요약

이 논문은 소프트웨어 시스템의 운영 상태를 나타내는 로그의 이상 탐지를 자동화하는 새로운 프레임워크인 RationAnomaly를 제안합니다. 기존의 딥러닝 모델은 해석 가능성과 일반화에 한계가 있고, 대형 언어 모델을 활용한 방법은 신뢰성과 사실적 정확성에서 문제를 겪습니다. RationAnomaly는 Chain-of-Thought(COT) 미세 조정과 강화 학습을 결합하여 이러한 문제를 해결합니다. 전문가 수준의 추론 패턴을 COT 기반 지도 학습으로 도입하고, 다각적 보상 함수를 사용하는 강화 학습 단계로 정확성과 논리적 일관성을 최적화합니다. 실험 결과, RationAnomaly는 주요 벤치마크에서 기존 최첨단 모델을 능가하는 F1 점수를 기록하며, 투명한 단계별 분석 결과를 제공합니다. 관련 코드와 데이터셋도 공개되었습니다.

## 🎯 주요 포인트

- 1. RationAnomaly는 Chain-of-Thought(CoT) 미세 조정과 강화 학습을 결합하여 로그 이상 탐지를 개선하는 새로운 프레임워크입니다.

- 2. CoT 기반의 지도 학습을 통해 전문가 수준의 추론 패턴을 주입하며, 엄격한 전문가 주도의 과정으로 교정된 고품질 데이터셋을 사용합니다.

- 3. 강화 학습 단계에서는 다면적인 보상 함수를 통해 정확성과 논리적 일관성을 최적화하여 환각 문제를 효과적으로 완화합니다.

- 4. RationAnomaly는 주요 벤치마크에서 최첨단 기준을 능가하는 F1 점수를 달성하며, 투명하고 단계별 분석 출력을 제공합니다.

- 5. 관련 코드와 데이터셋을 포함한 자원을 공개하였습니다.

---

*Generated on 2025-09-19 18:10:34*