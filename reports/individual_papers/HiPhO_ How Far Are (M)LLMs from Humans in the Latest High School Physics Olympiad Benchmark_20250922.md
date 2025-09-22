# HiPhO: How Far Are (M)LLMs from Humans in the Latest High School Physics Olympiad Benchmark?

**Korean Title:** HiPhO: 최신 고등학교 물리 올림피아드 벤치마크에서 (M)LLM은 인간과 얼마나 거리가 있는가?

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Olympiad Performance Comparison

## 🔗 유사한 논문
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (81.5% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (79.3% similar)
- [[2025-09-18/The NazoNazo Benchmark_ A Cost-Effective and Extensible Test of Insight-Based Reasoning in LLMs_20250918|The NazoNazo Benchmark A Cost-Effective and Extensible Test of Insight-Based Reasoning in LLMs]] (79.1% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (77.9% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (77.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07894v4 Announce Type: replace 
Abstract: Recently, the physical capabilities of (M)LLMs have garnered increasing attention. However, existing benchmarks for physics suffer from two major gaps: they neither provide systematic and up-to-date coverage of real-world physics competitions such as physics Olympiads, nor enable direct performance comparison with humans. To bridge these gaps, we present HiPhO, the first benchmark dedicated to high school physics Olympiads with human-aligned evaluation. Specifically, HiPhO highlights three key innovations. (1) Comprehensive Data: It compiles 13 latest Olympiad exams from 2024-2025, spanning both international and regional competitions, and covering mixed modalities that encompass problems spanning text-only to diagram-based. (2) Professional Evaluation: We adopt official marking schemes to perform fine-grained grading at both the answer and step level, fully aligned with human examiners to ensure high-quality and domain-specific evaluation. (3) Comparison with Human Contestants: We assign gold, silver, and bronze medals to models based on official medal thresholds, thereby enabling direct comparison between (M)LLMs and human contestants. Our large-scale evaluation of 30 state-of-the-art (M)LLMs shows that: across 13 exams, open-source MLLMs mostly remain at or below the bronze level; open-source LLMs show promising progress with multiple golds; closed-source reasoning MLLMs can achieve 6 to 12 gold medals; and most models still have a significant gap from full marks. These results highlight the performance gap between open-source models and top students, the strong reasoning abilities of closed-source models, and the remaining room for improvement. HiPhO, a human-aligned Olympiad benchmark for multimodal physical reasoning, is open-source at https://github.com/SciYu/HiPhO with a public leaderboard at https://phyarena.github.io/.

## 🔍 Abstract (한글 번역)

arXiv:2509.07894v4 발표 유형: 교체  
초록: 최근 (M)LLM의 물리적 능력에 대한 관심이 증가하고 있습니다. 그러나 기존의 물리학 벤치마크는 두 가지 주요 결함이 있습니다. 첫째, 물리학 올림피아드와 같은 실제 물리학 대회에 대한 체계적이고 최신의 포괄성을 제공하지 않으며, 둘째, 인간과의 직접적인 성능 비교를 가능하게 하지 않습니다. 이러한 격차를 해소하기 위해, 우리는 인간 정렬 평가를 갖춘 고등학교 물리학 올림피아드에 전념하는 최초의 벤치마크인 HiPhO를 소개합니다. 구체적으로, HiPhO는 세 가지 주요 혁신을 강조합니다. (1) 포괄적인 데이터: 2024-2025년의 최신 올림피아드 시험 13개를 국제 및 지역 대회를 포함하여 수집하며, 텍스트 전용 문제부터 다이어그램 기반 문제에 이르는 혼합 모달리티를 포함합니다. (2) 전문 평가: 공식 채점 방식을 채택하여 답변 및 단계 수준에서 세밀한 채점을 수행하며, 인간 채점자와 완전히 일치하여 고품질의 도메인 특화 평가를 보장합니다. (3) 인간 참가자와의 비교: 공식 메달 기준에 따라 모델에 금, 은, 동메달을 부여하여 (M)LLM과 인간 참가자 간의 직접 비교를 가능하게 합니다. 30개의 최신 (M)LLM에 대한 대규모 평가 결과: 13개의 시험에서 오픈 소스 MLLM은 대부분 동메달 수준에 머물거나 그 이하이며, 오픈 소스 LLM은 여러 개의 금메달을 획득하며 유망한 진전을 보입니다. 폐쇄형 추론 MLLM은 6개에서 12개의 금메달을 달성할 수 있으며, 대부분의 모델은 여전히 만점과 상당한 격차가 있습니다. 이러한 결과는 오픈 소스 모델과 최상위 학생 간의 성능 격차, 폐쇄형 모델의 강력한 추론 능력, 그리고 개선의 여지를 강조합니다. HiPhO는 다중 모달 물리적 추론을 위한 인간 정렬 올림피아드 벤치마크로, https://github.com/SciYu/HiPhO에서 오픈 소스로 제공되며, 공개 리더보드는 https://phyarena.github.io/에서 확인할 수 있습니다.

## 📝 요약

최근 물리학 분야에서 대형 언어 모델(MLLMs)의 능력이 주목받고 있지만, 기존의 물리학 벤치마크는 실제 물리학 대회에 대한 체계적이고 최신의 평가를 제공하지 못하며 인간과의 직접적인 성능 비교도 어렵습니다. 이를 해결하기 위해, 우리는 고등학교 물리 올림피아드를 위한 최초의 벤치마크인 HiPhO를 제안합니다. HiPhO는 최신 올림피아드 시험 13개를 포함하며, 공식 채점 기준을 사용해 인간과 일치하는 평가를 수행하고, 모델에 금, 은, 동메달을 부여하여 인간 참가자와의 직접 비교를 가능하게 합니다. 30개의 최신 MLLM을 평가한 결과, 오픈 소스 MLLM은 대부분 동메달 수준에 머물렀고, 폐쇄형 모델은 최대 12개의 금메달을 획득할 수 있었습니다. 이는 오픈 소스 모델과 최상위 학생 간의 성능 차이와 폐쇄형 모델의 강력한 추론 능력을 보여줍니다. HiPhO는 https://github.com/SciYu/HiPhO에서 공개되어 있으며, 공개 리더보드도 제공됩니다.

## 🎯 주요 포인트

- 1. HiPhO는 물리 올림피아드를 위한 최초의 벤치마크로, 인간과의 성능 비교를 가능하게 합니다.

- 2. 이 벤치마크는 2024-2025년의 최신 올림피아드 시험 13개를 포함하여 다양한 문제 유형을 포괄합니다.

- 3. 공식 채점 기준을 사용하여 인간 채점자와 일치하는 정밀한 평가를 수행합니다.

- 4. 모델 성능을 인간 참가자와 비교하기 위해 공식 메달 기준에 따라 금, 은, 동메달을 부여합니다.

- 5. 대규모 평가 결과, 오픈 소스 모델은 주로 동메달 수준에 머물렀으며, 폐쇄형 모델은 최대 12개의 금메달을 획득할 수 있었습니다.

---

*Generated on 2025-09-22 14:34:09*