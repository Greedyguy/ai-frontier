# Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses

**Korean Title:** 포인트와이즈 점수를 넘어서: LLM 응답의 분해된 기준 기반 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Decomposed Criteria Based Evaluation

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (83.5% similar)
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (83.0% similar)
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era A Survey]] (81.8% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (81.4% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (81.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16093v1 Announce Type: cross 
Abstract: Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single undifferentiated score. We introduce DeCE, a decomposed LLM evaluation framework that separates precision (factual accuracy and relevance) and recall (coverage of required concepts), using instance-specific criteria automatically extracted from gold answer requirements. DeCE is model-agnostic and domain-general, requiring no predefined taxonomies or handcrafted rubrics. We instantiate DeCE to evaluate different LLMs on a real-world legal QA task involving multi-jurisdictional reasoning and citation grounding. DeCE achieves substantially stronger correlation with expert judgments ($r=0.78$), compared to traditional metrics ($r=0.12$), pointwise LLM scoring ($r=0.35$), and modern multidimensional evaluators ($r=0.48$). It also reveals interpretable trade-offs: generalist models favor recall, while specialized models favor precision. Importantly, only 11.95% of LLM-generated criteria required expert revision, underscoring DeCE's scalability. DeCE offers an interpretable and actionable LLM evaluation framework in expert domains.

## 🔍 Abstract (한글 번역)

arXiv:2509.16093v1 발표 유형: 교차  
초록: 법률이나 의학과 같은 고위험 분야에서의 장문 답변 평가에는 여전히 근본적인 어려움이 존재합니다. BLEU와 ROUGE와 같은 표준 지표는 의미적 정확성을 포착하지 못하며, 현재의 대형 언어 모델(LLM) 기반 평가자들은 종종 답변 품질의 미묘한 측면을 단일한 점수로 축소합니다. 우리는 정확도(사실적 정확성과 관련성)와 재현율(필요한 개념의 포괄성)을 분리하여, 금본 답변 요구사항에서 자동으로 추출된 사례별 기준을 사용하는 분해된 LLM 평가 프레임워크인 DeCE를 소개합니다. DeCE는 모델에 구애받지 않으며, 사전 정의된 분류 체계나 수작업으로 만든 평가표가 필요하지 않은 일반적인 도메인에 적용 가능합니다. 우리는 다중 관할권적 추론과 인용 근거를 포함하는 실제 법률 QA 작업에서 다양한 LLM을 평가하기 위해 DeCE를 구현했습니다. DeCE는 전문가 판단과의 상관관계에서 전통적인 지표($r=0.12$), 점별 LLM 점수화($r=0.35$), 현대적 다차원 평가자($r=0.48$)에 비해 상당히 강한 상관관계($r=0.78$)를 달성했습니다. 또한 해석 가능한 절충점을 드러냅니다: 일반 모델은 재현율을 선호하고, 전문 모델은 정확도를 선호합니다. 중요한 점은, LLM이 생성한 기준 중 전문가 수정이 필요한 경우가 11.95%에 불과하여 DeCE의 확장 가능성을 강조합니다. DeCE는 전문가 도메인에서 해석 가능하고 실행 가능한 LLM 평가 프레임워크를 제공합니다.

## 📝 요약

이 논문은 법률 및 의학과 같은 고위험 분야에서 장문의 답변 평가의 어려움을 다룹니다. 기존의 BLEU 및 ROUGE 지표는 의미적 정확성을 포착하지 못하며, 현재의 대형 언어 모델(LLM) 기반 평가자들은 답변의 질을 단일 점수로 축소하는 한계가 있습니다. 이를 해결하기 위해, 이 논문은 DeCE라는 평가 프레임워크를 제안합니다. DeCE는 정밀도(사실적 정확성과 관련성)와 재현율(필요한 개념의 포괄성)을 분리하여 평가하며, 금 답변 요구사항에서 자동으로 추출된 기준을 사용합니다. 이 프레임워크는 모델에 구애받지 않고, 사전 정의된 분류체계나 수작업 평가 기준이 필요 없습니다. 실제 법률 QA 작업에 적용한 결과, DeCE는 전문가 평가와 높은 상관관계($r=0.78$)를 보였으며, 기존 지표나 다른 평가 방법들보다 우수한 성능을 나타냈습니다. 또한, 일반 모델은 재현율을, 특화 모델은 정밀도를 중시하는 경향을 밝혀냈습니다. DeCE는 전문가 도메인에서 해석 가능하고 실행 가능한 평가 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. DeCE는 법률 및 의학과 같은 고위험 분야에서 긴 형식의 답변을 평가하기 위해 정밀도와 재현율을 분리하여 평가하는 LLM 기반 프레임워크입니다.

- 2. DeCE는 모델에 구애받지 않고, 사전 정의된 분류체계나 수작업으로 작성된 평가 기준이 필요하지 않은 범용적인 평가 방법을 제공합니다.

- 3. 실제 법률 QA 작업에서 DeCE는 전문가 판단과의 상관관계가 $r=0.78$로, 전통적인 평가 지표 및 현대적 평가자들보다 훨씬 높은 상관관계를 보였습니다.

- 4. DeCE는 일반 모델이 재현율을, 전문 모델이 정밀도를 선호하는 해석 가능한 균형점을 드러냅니다.

- 5. LLM이 생성한 기준 중 전문가 수정이 필요한 경우는 11.95%에 불과하여 DeCE의 확장 가능성을 강조합니다.

---

*Generated on 2025-09-22 14:24:50*