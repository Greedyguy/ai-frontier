# BEFT: Bias-Efficient Fine-Tuning of Language Models

**Korean Title:** BEFT: 언어 모델의 편향 효율적 미세 조정

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Parameter Efficient Fine Tuning

## 🔗 유사한 논문
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (82.7% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.3% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.0% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (81.0% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15974v1 Announce Type: cross 
Abstract: Fine-tuning all-bias-terms stands out among various parameter-efficient fine-tuning (PEFT) techniques, owing to its out-of-the-box usability and competitive performance, especially in low-data regimes. Bias-only fine-tuning has the potential for unprecedented parameter efficiency. However, the link between fine-tuning different bias terms (i.e., bias terms in the query, key, or value projections) and downstream performance remains unclear. The existing approaches, e.g., based on the magnitude of bias change or empirical Fisher information, provide limited guidance for selecting the particular bias term for effective fine-tuning. In this paper, we propose an approach for selecting the bias term to be fine-tuned, forming the foundation of our bias-efficient fine-tuning (BEFT). We extensively evaluate our bias-efficient approach against other bias-selection approaches, across a wide range of large language models (LLMs) spanning encoder-only and decoder-only architectures from 110M to 6.7B parameters. Our results demonstrate the effectiveness and superiority of our bias-efficient approach on diverse downstream tasks, including classification, multiple-choice, and generation tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15974v1 발표 유형: 교차  
초록: 모든 바이어스 항목을 미세 조정하는 것은 다양한 파라미터 효율적 미세 조정(PEFT) 기법 중에서 특히 저데이터 환경에서의 즉시 사용 가능성과 경쟁력 있는 성능 덕분에 두드러집니다. 바이어스 전용 미세 조정은 전례 없는 파라미터 효율성을 제공할 잠재력을 가지고 있습니다. 그러나 서로 다른 바이어스 항목(즉, 쿼리, 키, 또는 값 투영의 바이어스 항목)을 미세 조정하는 것과 다운스트림 성능 간의 연결은 명확하지 않습니다. 바이어스 변화의 크기나 경험적 피셔 정보에 기반한 기존 접근법은 효과적인 미세 조정을 위한 특정 바이어스 항목을 선택하는 데 제한된 지침을 제공합니다. 본 논문에서는 미세 조정할 바이어스 항목을 선택하는 접근법을 제안하며, 이는 우리의 바이어스 효율적 미세 조정(BEFT)의 기초를 형성합니다. 우리는 인코더 전용 및 디코더 전용 아키텍처를 포함하여 110M에서 6.7B 파라미터에 이르는 다양한 대형 언어 모델(LLM)을 대상으로 다른 바이어스 선택 접근법과 비교하여 우리의 바이어스 효율적 접근법을 광범위하게 평가했습니다. 우리의 결과는 분류, 다중 선택, 생성 작업을 포함한 다양한 다운스트림 작업에서 우리의 바이어스 효율적 접근법의 효과성과 우수성을 입증합니다.

## 📝 요약

이 논문은 파라미터 효율적인 미세 조정(PEFT) 기법 중 하나인 모든 바이어스 항목의 미세 조정에 대해 다룹니다. 특히, 데이터가 적은 환경에서 경쟁력 있는 성능을 보이며, 바이어스 항목만을 조정하는 것이 파라미터 효율성을 극대화할 잠재력을 가지고 있습니다. 그러나 쿼리, 키, 값 프로젝션의 바이어스 항목을 조정하는 것이 실제 성능에 미치는 영향은 명확하지 않았습니다. 기존 접근법은 특정 바이어스 항목을 선택하는 데 제한적인 지침만 제공했습니다. 본 연구에서는 바이어스 항목 선택을 위한 새로운 접근법을 제안하며, 이를 바탕으로 한 바이어스 효율적 미세 조정(BEFT)을 소개합니다. 다양한 대형 언어 모델(LLM)을 대상으로 한 실험 결과, 제안된 방법이 분류, 다중 선택, 생성 작업 등 다양한 다운스트림 작업에서 효과적이고 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 모든 바이어스 항목을 미세 조정하는 방법은 낮은 데이터 환경에서 경쟁력 있는 성능을 보여주는 파라미터 효율적인 미세 조정 기법 중 하나입니다.

- 2. 바이어스 항목만을 미세 조정하는 것은 전례 없는 파라미터 효율성을 제공할 잠재력을 가지고 있습니다.

- 3. 본 논문에서는 효과적인 미세 조정을 위한 특정 바이어스 항목 선택에 대한 새로운 접근 방식을 제안합니다.

- 4. 제안된 바이어스 효율적 미세 조정(BEFT) 접근 방식은 다양한 대형 언어 모델(LLM)에서 다른 바이어스 선택 접근 방식과 비교하여 우수한 성능을 입증합니다.

- 5. 제안된 방법은 분류, 다중 선택, 생성 작업을 포함한 다양한 다운스트림 작업에서 효과적이고 우수한 성능을 보입니다.

---

*Generated on 2025-09-22 14:20:17*