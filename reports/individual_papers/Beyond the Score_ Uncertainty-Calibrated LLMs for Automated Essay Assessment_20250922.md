# Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment

**Korean Title:** 점수를 넘어서: 자동화된 에세이 평가를 위한 불확실성 보정 대형 언어 모델(LLM)

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Conformal Prediction|Conformal Prediction]] [[keywords/specific/Uncertainty-aware Accuracy|Uncertainty-aware Accuracy]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Automated Essay Scoring|Automated Essay Scoring]] [[categories/cs.LG|cs.LG]] [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (85.3% similar) [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (83.4% similar) [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Conformal Prediction, Uncertainty-aware Accuracy
**🔬 Broad Technical**: Large Language Models, Automated Essay Scoring
## 🔗 유사한 논문
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (85.3% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025 Towards Uncertainty Aware Arabic Readability Assessment]] (83.4% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.2% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (81.8% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.5% similar)


**ArXiv ID**: [2509.15926](https://arxiv.org/abs/2509.15926)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15926.pdf)


**ArXiv ID**: [2509.15926](https://arxiv.org/abs/2509.15926)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15926.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Conformal Prediction
**⭐ Unique Technical**: Uncertainty-aware Accuracy
**🔬 Broad Technical**: Large Language Models, Automated Essay Scoring

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Automated Essay Scoring` • 

`Conformal Prediction` • 

`Uncertainty-aware Accuracy`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15926v1 Announce Type: cross 
Abstract: Automated Essay Scoring (AES) systems now reach near human agreement on some public benchmarks, yet real-world adoption, especially in high-stakes examinations, remains limited. A principal obstacle is that most models output a single score without any accompanying measure of confidence or explanation. We address this gap with conformal prediction, a distribution-free wrapper that equips any classifier with set-valued outputs and formal coverage guarantees. Two open-source large language models (Llama-3 8B and Qwen-2.5 3B) are fine-tuned on three diverse corpora (ASAP, TOEFL11, Cambridge-FCE) and calibrated at a 90 percent risk level. Reliability is assessed with UAcc, an uncertainty-aware accuracy that rewards models for being both correct and concise. To our knowledge, this is the first work to combine conformal prediction and UAcc for essay scoring. The calibrated models consistently meet the coverage target while keeping prediction sets compact, indicating that open-source, mid-sized LLMs can already support teacher-in-the-loop AES; we discuss scaling and broader user studies as future work.

## 🔍 Abstract (한글 번역)

arXiv:2509.15926v1 발표 유형: 교차  
초록: 자동 에세이 채점(AES) 시스템은 이제 일부 공공 벤치마크에서 인간과 거의 일치하는 수준에 도달했지만, 실제 세계에서의 채택, 특히 고위험 시험에서는 여전히 제한적입니다. 주요 장애물은 대부분의 모델이 신뢰도나 설명 없이 단일 점수만을 출력한다는 점입니다. 우리는 이 격차를 보완하기 위해 모든 분류기에 집합 값 출력과 공식적인 커버리지 보장을 제공하는 분포 자유 래퍼인 적합 예측(conformal prediction)을 사용합니다. 두 개의 오픈 소스 대형 언어 모델(Llama-3 8B 및 Qwen-2.5 3B)은 세 가지 다양한 코퍼스(ASAP, TOEFL11, Cambridge-FCE)에서 미세 조정되고 90퍼센트 위험 수준에서 보정됩니다. 신뢰성은 모델이 정확하고 간결할 때 보상을 받는 불확실성 인식 정확도(UAcc)로 평가됩니다. 우리의 지식으로는, 에세이 채점에 적합 예측과 UAcc를 결합한 첫 번째 연구입니다. 보정된 모델은 일관되게 커버리지 목표를 충족하면서 예측 집합을 간결하게 유지하여, 오픈 소스 중간 크기 LLM이 이미 교사 참여 AES를 지원할 수 있음을 나타냅니다. 우리는 확장 및 더 넓은 사용자 연구를 향후 작업으로 논의합니다.

## 📝 요약

이 논문은 자동 에세이 채점(AES) 시스템의 신뢰성과 설명 가능성을 높이기 위해, 기존 모델이 단일 점수만 출력하는 문제를 해결하고자 합니다. 이를 위해, 분포에 구애받지 않는 적합 예측(conformal prediction) 기법을 사용하여 모델에 세트 값 출력과 공식적인 커버리지 보장을 제공합니다. Llama-3 8B와 Qwen-2.5 3B라는 두 개의 오픈소스 대형 언어 모델을 다양한 코퍼스(ASAP, TOEFL11, Cambridge-FCE)로 미세 조정하고, 90%의 위험 수준에서 보정했습니다. 신뢰성은 불확실성 인식 정확도(UAcc)를 통해 평가되며, 이 연구는 적합 예측과 UAcc를 에세이 채점에 결합한 최초의 사례입니다. 보정된 모델은 커버리지 목표를 일관되게 달성하면서 예측 세트를 간결하게 유지하여, 오픈소스 중형 LLM이 교사 참여 AES를 지원할 수 있음을 보여줍니다. 향후 연구로는 확장성과 사용자 연구를 제안합니다.

## 🎯 주요 포인트


- 1. 자동 에세이 채점 시스템(AES)은 일부 공개 벤치마크에서 인간과 유사한 수준의 일치를 보이지만, 실제 고위험 시험에서는 여전히 채택이 제한적입니다.

- 2. 대부분의 모델이 단일 점수만 출력하고 자신감이나 설명을 제공하지 않는 것이 주요 장애물로 작용하고 있습니다.

- 3. 본 연구는 모든 분류기에 세트 값 출력과 형식적 커버리지 보장을 제공하는 분포-자유 래퍼인 적합 예측을 통해 이 문제를 해결합니다.

- 4. 두 개의 오픈 소스 대형 언어 모델(Llama-3 8B와 Qwen-2.5 3B)을 다양한 코퍼스에 맞춰 미세 조정하고 90% 위험 수준에서 보정하였습니다.

- 5. 본 연구는 적합 예측과 불확실성 인식 정확도(UAcc)를 에세이 채점에 결합한 최초의 연구로, 보정된 모델은 커버리지 목표를 일관되게 충족하면서 예측 세트를 간결하게 유지합니다.


---

*Generated on 2025-09-22 15:44:17*