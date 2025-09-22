
# MedVAL: Toward Expert-Level Medical Text Validation with Language Models

**Korean Title:** MedVAL: 언어 모델을 활용한 전문가 수준의 의료 텍스트 검증을 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: LM-as-judge Paradigm

## 🔗 유사한 논문
- [[A Comprehensive Survey on the Trustworthiness of Large Language Models in Healthcare]] (85.6% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (83.3% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.1% similar)
- [[CyberLLMInstruct A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (82.7% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (82.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.03152v4 Announce Type: replace-cross 
Abstract: With the growing use of language models (LMs) in clinical environments, there is an immediate need to evaluate the accuracy and safety of LM-generated medical text. Currently, such evaluation relies solely on manual physician review. However, detecting errors in LM-generated text is challenging because 1) manual review is costly and 2) expert-composed reference outputs are often unavailable in real-world settings. While the "LM-as-judge" paradigm (a LM evaluating another LM) offers scalable evaluation, even frontier LMs can miss subtle but clinically significant errors. To address these challenges, we propose MedVAL, a novel, self-supervised, data-efficient distillation method that leverages synthetic data to train evaluator LMs to assess whether LM-generated medical outputs are factually consistent with inputs, without requiring physician labels or reference outputs. To evaluate LM performance, we introduce MedVAL-Bench, a dataset of 840 physician-annotated outputs across 6 diverse medical tasks capturing real-world challenges. Across 10 state-of-the-art LMs spanning open-source and proprietary models, MedVAL distillation significantly improves (p < 0.001) alignment with physicians across seen and unseen tasks, increasing average F1 scores from 66% to 83%. Despite strong baseline performance, MedVAL improves the best-performing proprietary LM (GPT-4o) by 8% without training on physician-labeled data, demonstrating a performance statistically non-inferior to a single human expert (p < 0.001). To support a scalable, risk-aware pathway towards clinical integration, we open-source: 1) Codebase (https://github.com/StanfordMIMI/MedVAL), 2) MedVAL-Bench (https://huggingface.co/datasets/stanfordmimi/MedVAL-Bench), 3) MedVAL-4B (https://huggingface.co/stanfordmimi/MedVAL-4B). Our benchmark provides evidence of LMs approaching expert-level ability in validating AI-generated medical text.

## 🔍 Abstract (한글 번역)

arXiv:2507.03152v4 발표 유형: 교차 교체  
초록: 임상 환경에서 언어 모델(LM)의 사용이 증가함에 따라, LM이 생성한 의료 텍스트의 정확성과 안전성을 평가할 필요성이 즉각적으로 대두되고 있습니다. 현재 이러한 평가는 전적으로 의사의 수작업 검토에 의존하고 있습니다. 그러나 LM이 생성한 텍스트에서 오류를 감지하는 것은 1) 수작업 검토가 비용이 많이 들고 2) 전문가가 작성한 참조 출력물이 실제 환경에서 종종 제공되지 않기 때문에 어려운 과제입니다. "LM-as-judge" 패러다임(LM이 다른 LM을 평가하는 방식)은 확장 가능한 평가를 제공하지만, 최첨단 LM조차도 미묘하지만 임상적으로 중요한 오류를 놓칠 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 MedVAL이라는 새로운 자가 지도, 데이터 효율적인 증류 방법을 제안합니다. 이 방법은 합성 데이터를 활용하여 평가자 LM이 의사 레이블이나 참조 출력 없이 LM이 생성한 의료 출력물이 입력과 사실적으로 일치하는지를 평가하도록 훈련합니다. LM 성능을 평가하기 위해, 우리는 6개의 다양한 의료 과제에서 실제 문제를 포착한 840개의 의사 주석 출력물로 구성된 데이터셋인 MedVAL-Bench를 소개합니다. 오픈 소스 및 독점 모델을 아우르는 10개의 최첨단 LM에 걸쳐, MedVAL 증류는 보이는 과제와 보이지 않는 과제 모두에서 의사와의 정렬을 유의미하게 개선(p < 0.001)하며, 평균 F1 점수를 66%에서 83%로 증가시킵니다. 강력한 기본 성능에도 불구하고, MedVAL은 의사 레이블 데이터로 훈련하지 않고도 가장 성능이 뛰어난 독점 LM(GPT-4o)을 8% 개선하며, 단일 인간 전문가와 통계적으로 열등하지 않은 성능을 보여줍니다(p < 0.001). 임상 통합을 위한 확장 가능하고 위험 인식이 있는 경로를 지원하기 위해, 우리는 다음을 오픈 소스로 제공합니다: 1) 코드베이스 (https://github.com/StanfordMIMI/MedVAL), 2) MedVAL-Bench (https://huggingface.co/datasets/stanfordmimi/MedVAL-Bench), 3) MedVAL-4B (https://huggingface.co/stanfordmimi/MedVAL-4B). 우리의 벤치마크는 AI가 생성한 의료 텍스트를 검증하는 데 있어 LM이 전문가 수준의 능력에 접근하고 있음을 입증합니다.

## 📝 요약

이 논문은 임상 환경에서 사용되는 언어 모델(LM)의 정확성과 안전성을 평가하기 위한 새로운 방법론인 MedVAL을 제안합니다. MedVAL은 합성 데이터를 활용한 자기 지도 학습 방식으로, 의사 레이블이나 참조 출력 없이 LM이 생성한 의료 텍스트의 사실적 일관성을 평가하도록 훈련합니다. 이를 검증하기 위해 MedVAL-Bench라는 데이터셋을 도입하여 다양한 의료 과제에서 LM의 성능을 평가했습니다. MedVAL은 10개의 최신 LM에서 평균 F1 점수를 66%에서 83%로 향상시켰으며, 특히 GPT-4o 모델의 성능을 8% 개선했습니다. 이 연구는 LM이 전문가 수준의 능력에 근접했음을 보여주며, 코드베이스와 데이터셋을 공개하여 임상 통합을 위한 확장 가능한 경로를 지원합니다.

## 🎯 주요 포인트

- 1. 임상 환경에서 언어 모델(LM)의 사용이 증가함에 따라 LM이 생성한 의료 텍스트의 정확성과 안전성을 평가할 필요성이 대두되고 있습니다.

- 2. MedVAL은 의사 레이블이나 참조 출력 없이 LM 생성 의료 출력이 입력과 사실적으로 일치하는지 평가하기 위해 합성 데이터를 활용하는 새로운 자기 지도 학습 방법입니다.

- 3. MedVAL-Bench는 6가지 다양한 의료 과제에서 840개의 의사 주석 출력을 포함한 데이터셋으로, LM 성능을 평가하기 위한 도구로 사용됩니다.

- 4. MedVAL 증류 방법은 최첨단 LMs의 평균 F1 점수를 66%에서 83%로 향상시키며, 의사 레이블 데이터 없이도 최고의 성능을 보이는 독점 LM(GPT-4o)을 8% 개선합니다.

- 5. MedVAL의 오픈 소스 자원은 임상 통합을 위한 확장 가능하고 위험 인식 경로를 지원하며, AI 생성 의료 텍스트 검증에서 전문가 수준의 능력에 접근하고 있음을 보여줍니다.

---

*Generated on 2025-09-19 15:18:19*