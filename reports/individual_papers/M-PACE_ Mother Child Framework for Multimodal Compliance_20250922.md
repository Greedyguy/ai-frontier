# M-PACE: Mother Child Framework for Multimodal Compliance

**Korean Title:** M-PACE: 다중 모달 준수를 위한 모자 프레임워크

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Mother Child MLLM Setup|Mother Child MLLM Setup]] [[keywords/specific/Vision-Language Inputs|Vision-Language Inputs]] [[keywords/broad/Multimodal Large Language Models|Multimodal Large Language Models]] [[keywords/broad/Compliance Framework|Compliance Framework]] [[keywords/unique/Multimodal Parameter Agnostic Compliance Engine|Multimodal Parameter Agnostic Compliance Engine]] [[categories/cs.CL|cs.CL]] [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (83.5% similar) [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (83.1% similar) [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Inputs
**🔗 Specific Connectable**: Compliance Framework
**🔬 Broad Technical**: Multimodal Large Language Models
**⭐ Unique Technical**: M-PACE
## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (83.5% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (83.1% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.7% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (82.4% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (82.2% similar)


**ArXiv ID**: [2509.15241](https://arxiv.org/abs/2509.15241)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15241.pdf)


**ArXiv ID**: [2509.15241](https://arxiv.org/abs/2509.15241)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15241.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Inputs
**🔗 Specific Connectable**: Compliance Framework
**⭐ Unique Technical**: M-PACE
**🔬 Broad Technical**: Multimodal Large Language Models

## 🏷️ 추출된 키워드



`Multimodal Large Language Models` • 

`Image Classification` • 

`Text Extraction` • 

`Multimodal Parameter Agnostic Compliance Engine` • 

`Vision-Language Inputs`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15241v1 Announce Type: cross 
Abstract: Ensuring that multi-modal content adheres to brand, legal, or platform-specific compliance standards is an increasingly complex challenge across domains. Traditional compliance frameworks typically rely on disjointed, multi-stage pipelines that integrate separate modules for image classification, text extraction, audio transcription, hand-crafted checks, and rule-based merges. This architectural fragmentation increases operational overhead, hampers scalability, and hinders the ability to adapt to dynamic guidelines efficiently. With the emergence of Multimodal Large Language Models (MLLMs), there is growing potential to unify these workflows under a single, general-purpose framework capable of jointly processing visual and textual content. In light of this, we propose Multimodal Parameter Agnostic Compliance Engine (M-PACE), a framework designed for assessing attributes across vision-language inputs in a single pass. As a representative use case, we apply M-PACE to advertisement compliance, demonstrating its ability to evaluate over 15 compliance-related attributes. To support structured evaluation, we introduce a human-annotated benchmark enriched with augmented samples that simulate challenging real-world conditions, including visual obstructions and profanity injection. M-PACE employs a mother-child MLLM setup, demonstrating that a stronger parent MLLM evaluating the outputs of smaller child models can significantly reduce dependence on human reviewers, thereby automating quality control. Our analysis reveals that inference costs reduce by over 31 times, with the most efficient models (Gemini 2.0 Flash as child MLLM selected by mother MLLM) operating at 0.0005 per image, compared to 0.0159 for Gemini 2.5 Pro with comparable accuracy, highlighting the trade-off between cost and output quality achieved in real time by M-PACE in real life deployment over advertising data.

## 🔍 Abstract (한글 번역)

arXiv:2509.15241v1 발표 유형: 교차  
초록: 다중 모달 콘텐츠가 브랜드, 법률 또는 플랫폼별 준수 기준을 충족하도록 보장하는 것은 다양한 분야에서 점점 더 복잡한 과제가 되고 있습니다. 전통적인 준수 프레임워크는 일반적으로 이미지 분류, 텍스트 추출, 오디오 전사, 수작업 검사 및 규칙 기반 병합을 위한 개별 모듈을 통합하는 분리된 다단계 파이프라인에 의존합니다. 이러한 구조적 분열은 운영 비용을 증가시키고, 확장성을 저해하며, 동적인 지침에 효율적으로 적응하는 능력을 방해합니다. 다중 모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)의 출현으로, 시각적 및 텍스트 콘텐츠를 공동으로 처리할 수 있는 단일의 범용 프레임워크 하에 이러한 워크플로를 통합할 수 있는 잠재력이 커지고 있습니다. 이에 따라 우리는 시각-언어 입력의 속성을 단일 패스로 평가하도록 설계된 다중 모달 매개변수 비인식 준수 엔진(Multimodal Parameter Agnostic Compliance Engine, M-PACE)을 제안합니다. 대표적인 사용 사례로, 우리는 광고 준수에 M-PACE를 적용하여 15개 이상의 준수 관련 속성을 평가할 수 있음을 입증합니다. 구조화된 평가를 지원하기 위해, 시각적 장애물 및 비속어 삽입을 포함한 도전적인 실제 조건을 시뮬레이션하는 증강 샘플로 풍부해진 인간 주석 벤치마크를 도입합니다. M-PACE는 모자(Mother-Child) MLLM 설정을 사용하여, 더 강력한 모(Mother) MLLM이 더 작은 자식(Child) 모델의 출력을 평가하는 방식이 인간 검토자에 대한 의존도를 크게 줄이고 품질 관리를 자동화할 수 있음을 보여줍니다. 우리의 분석에 따르면, 추론 비용이 31배 이상 감소하며, 가장 효율적인 모델(Gemini 2.0 Flash가 모 MLLM에 의해 선택된 자식 MLLM으로 작동)이 이미지당 0.0005로 운영되는 반면, 유사한 정확도를 가진 Gemini 2.5 Pro는 0.0159를 기록하여, 광고 데이터에 대한 실제 배포에서 M-PACE가 실시간으로 달성한 비용과 출력 품질 간의 균형을 강조합니다.

## 📝 요약

이 논문은 멀티모달 콘텐츠가 브랜드, 법적, 플랫폼별 규정을 준수하도록 보장하는 새로운 프레임워크인 M-PACE를 제안합니다. 전통적인 규정 준수 시스템은 이미지 분류, 텍스트 추출, 오디오 전사 등 여러 모듈을 통합하여 복잡하고 비효율적입니다. M-PACE는 멀티모달 대형 언어 모델(MLLM)을 활용하여 시각 및 텍스트 콘텐츠를 단일 프레임워크에서 처리하며, 광고 규정 준수에 적용하여 15개 이상의 속성을 평가할 수 있음을 보여줍니다. 또한, 시뮬레이션된 현실적 조건을 포함한 벤치마크를 제시하여 성능을 검증합니다. M-PACE는 모자 관계의 MLLM 구조를 사용하여 인간 리뷰어의 의존도를 줄이고 품질 관리를 자동화하며, 비용을 31배 이상 절감할 수 있음을 입증합니다.

## 🎯 주요 포인트


- 1. 멀티모달 콘텐츠의 브랜드, 법률, 플랫폼 규정 준수를 보장하는 것은 점점 더 복잡한 과제가 되고 있다.

- 2. 전통적인 규정 준수 프레임워크는 이미지 분류, 텍스트 추출, 오디오 전사 등 분리된 모듈을 통합하는 다단계 파이프라인에 의존한다.

- 3. MLLM의 등장으로 시각적 및 텍스트 콘텐츠를 단일 프레임워크에서 처리할 수 있는 가능성이 커지고 있다.

- 4. M-PACE는 광고 준수를 위한 사용 사례로, 15개 이상의 규정 준수 관련 속성을 평가할 수 있다.

- 5. M-PACE는 인간 검토자 의존도를 줄이고 품질 관리를 자동화하여 추론 비용을 31배 이상 절감한다.


---

*Generated on 2025-09-22 16:31:24*