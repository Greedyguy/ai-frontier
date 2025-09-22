# LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models

**Korean Title:** LNE-Blocking: 대형 언어 모델에서 오염 완화 평가를 위한 효율적인 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Ruijie Hou|Ruijie Hou]] [[authors/Yueyang Jiao|Yueyang Jiao]] [[authors/Hanxu Hu|Hanxu Hu]] [[authors/Yingming Li|Yingming Li]] [[authors/Wai Lam|Wai Lam]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Contamination Mitigation

## 🔗 유사한 논문
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.0% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.7% similar)
- [[Assessing Historical Structural Oppression Worldwide via Rule-Guided Prompting of Large Language Models_20250919|Assessing Historical Structural Oppression Worldwide via Rule-Guided Prompting of Large Language Models]] (83.6% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (83.5% similar)
- [[ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (83.3% similar)

## 📋 저자 정보

**Authors:** Ruijie Hou, Yueyang Jiao, Hanxu Hu, Yingming Li, Wai Lam, Huajian Zhang, Hongyuan Lu

## 📄 Abstract (원문)

The problem of data contamination is now almost inevitable during the
development of large language models (LLMs), with the training data commonly
integrating those evaluation benchmarks even unintentionally. This problem
subsequently makes it hard to benchmark LLMs fairly. Instead of constructing
contamination-free datasets (quite hard), we propose a novel framework,
\textbf{LNE-Blocking}, to restore model performance prior to contamination on
potentially leaked datasets. Our framework consists of two components:
contamination detection and disruption operation. For the prompt, the framework
first uses the contamination detection method, \textbf{LNE}, to assess the
extent of contamination in the model. Based on this, it adjusts the intensity
of the disruption operation, \textbf{Blocking}, to elicit non-memorized
responses from the model. Our framework is the first to efficiently restore the
model's greedy decoding performance. This comes with a strong performance on
multiple datasets with potential leakage risks, and it consistently achieves
stable recovery results across different models and varying levels of data
contamination. We release the code at https://github.com/RuijieH/LNE-Blocking
to facilitate research.

## 🔍 Abstract (한글 번역)

데이터 오염 문제는 대규모 언어 모델(LLM)의 개발 과정에서 거의 불가피하게 발생하며, 훈련 데이터가 의도치 않게 평가 기준을 통합하는 경우가 흔합니다. 이 문제는 LLM을 공정하게 평가하기 어렵게 만듭니다. 오염이 없는 데이터셋을 구축하는 대신(이는 매우 어렵습니다), 우리는 잠재적으로 유출된 데이터셋에서 오염 이전의 모델 성능을 복원하기 위한 새로운 프레임워크, \textbf{LNE-Blocking}을 제안합니다. 우리의 프레임워크는 오염 탐지와 방해 작업의 두 가지 구성 요소로 이루어져 있습니다. 프롬프트에 대해, 프레임워크는 먼저 오염 탐지 방법인 \textbf{LNE}를 사용하여 모델의 오염 정도를 평가합니다. 이를 바탕으로, 모델로부터 비기억화된 응답을 이끌어내기 위해 방해 작업의 강도, \textbf{Blocking}을 조정합니다. 우리의 프레임워크는 모델의 탐욕적 디코딩 성능을 효율적으로 복원하는 최초의 방법입니다. 이는 잠재적 유출 위험이 있는 여러 데이터셋에서 강력한 성능을 보이며, 다양한 모델과 다양한 수준의 데이터 오염에 걸쳐 일관된 복구 결과를 지속적으로 달성합니다. 연구를 촉진하기 위해 코드를 https://github.com/RuijieH/LNE-Blocking에서 공개합니다.

## 📝 요약

대형 언어 모델(LLM)의 개발 과정에서 데이터 오염 문제는 거의 피할 수 없으며, 이는 평가 기준의 공정한 벤치마킹을 어렵게 만듭니다. 이를 해결하기 위해, 우리는 오염 없는 데이터셋을 만드는 대신, \textbf{LNE-Blocking}이라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 오염 감지와 방해 작업의 두 가지 구성 요소로 이루어져 있습니다. 먼저, \textbf{LNE} 방법을 통해 모델의 오염 정도를 평가하고, 이를 바탕으로 \textbf{Blocking} 작업의 강도를 조절하여 모델의 비기억 응답을 유도합니다. 이 프레임워크는 여러 데이터셋에서 강력한 성능을 보이며, 다양한 모델과 오염 수준에서도 안정적인 성능 회복을 달성합니다. 연구를 촉진하기 위해 코드를 공개했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM) 개발 시 데이터 오염 문제는 거의 불가피하며, 이는 공정한 벤치마킹을 어렵게 만듭니다.

- 2. 우리는 오염 없는 데이터셋을 만드는 대신, 잠재적으로 유출된 데이터셋에서 모델 성능을 복원하는 새로운 프레임워크인 LNE-Blocking을 제안합니다.

- 3. LNE-Blocking은 오염 감지와 방해 작업 두 가지 구성 요소로 이루어져 있으며, 모델의 기억되지 않은 응답을 유도합니다.

- 4. 이 프레임워크는 여러 데이터셋에서 강력한 성능을 보이며, 다양한 모델과 데이터 오염 수준에서도 안정적인 복구 결과를 일관되게 달성합니다.

- 5. 연구를 촉진하기 위해 LNE-Blocking의 코드를 공개합니다.

---

*Generated on 2025-09-20 00:49:12*