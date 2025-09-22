# Evaluating Robustness of LLMs in Question Answering on Multilingual Noisy OCR Data

**Korean Title:** 다국어 잡음이 있는 OCR 데이터에서 질문 응답에 대한 대형 언어 모델(LLM)의 강건성 평가

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Noise-resilient QA Systems|Noise-resilient QA Systems]] [[keywords/specific/OCR Noise Analysis|OCR Noise Analysis]] [[keywords/broad/Optical Character Recognition|Optical Character Recognition]] [[keywords/broad/Multilingual QA Systems|Multilingual QA Systems]] [[keywords/unique/MultiOCR-QA|MultiOCR-QA]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (83.5% similar) [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert]] (80.2% similar) [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Noise-resilient QA Systems
**🔗 Specific Connectable**: OCR-induced Noise
**🔬 Broad Technical**: Optical Character Recognition, Multilingual QA Systems
**⭐ Unique Technical**: MultiOCR-QA
## 🔗 유사한 논문
- [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (83.5% similar)
- [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise Asymmetric LoRA Adaption with Poisoning Expert]] (80.2% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (80.0% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (79.4% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (79.2% similar)


**ArXiv ID**: [2502.16781](https://arxiv.org/abs/2502.16781)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2502.16781.pdf)


**ArXiv ID**: [2502.16781](https://arxiv.org/abs/2502.16781)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2502.16781.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Noise-resilient QA Systems
**🔗 Specific Connectable**: OCR Noise Analysis
**⭐ Unique Technical**: MultiOCR-QA Dataset
**🔬 Broad Technical**: Optical Character Recognition, Multilingual QA Systems

## 🏷️ 추출된 키워드



`Optical Character Recognition` • 

`Multilingual Question Answering` • 

`OCR Noise Analysis` • 

`MultiOCR-QA Dataset` • 

`Noise-resilient QA Systems`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.16781v3 Announce Type: replace 
Abstract: Optical Character Recognition (OCR) plays a crucial role in digitizing historical and multilingual documents, yet OCR errors - imperfect extraction of text, including character insertion, deletion, and substitution can significantly impact downstream tasks like question-answering (QA). In this work, we conduct a comprehensive analysis of how OCR-induced noise affects the performance of Multilingual QA Systems. To support this analysis, we introduce a multilingual QA dataset MultiOCR-QA, comprising 50K question-answer pairs across three languages, English, French, and German. The dataset is curated from OCR-ed historical documents, which include different levels and types of OCR noise. We then evaluate how different state-of-the-art Large Language Models (LLMs) perform under different error conditions, focusing on three major OCR error types. Our findings show that QA systems are highly prone to OCR-induced errors and perform poorly on noisy OCR text. By comparing model performance on clean versus noisy texts, we provide insights into the limitations of current approaches and emphasize the need for more noise-resilient QA systems in historical digitization contexts.

## 🔍 Abstract (한글 번역)

arXiv:2502.16781v3 발표 유형: 교체  
초록: 광학 문자 인식(OCR)은 역사적 및 다국어 문서를 디지털화하는 데 중요한 역할을 하지만, 문자 삽입, 삭제 및 대체를 포함한 텍스트의 불완전한 추출인 OCR 오류는 질문-응답(QA)과 같은 후속 작업에 상당한 영향을 미칠 수 있습니다. 본 연구에서는 OCR로 인한 노이즈가 다국어 QA 시스템의 성능에 어떻게 영향을 미치는지에 대한 포괄적인 분석을 수행합니다. 이 분석을 지원하기 위해 영어, 프랑스어 및 독일어의 세 가지 언어로 50,000개의 질문-응답 쌍으로 구성된 다국어 QA 데이터셋 MultiOCR-QA를 소개합니다. 이 데이터셋은 다양한 수준과 유형의 OCR 노이즈를 포함한 OCR 처리된 역사적 문서에서 큐레이션되었습니다. 그런 다음, 우리는 세 가지 주요 OCR 오류 유형에 중점을 두고, 서로 다른 오류 조건 하에서 다양한 최신 대형 언어 모델(LLMs)이 어떻게 성능을 발휘하는지 평가합니다. 우리의 연구 결과는 QA 시스템이 OCR로 인한 오류에 매우 취약하며 노이즈가 있는 OCR 텍스트에서 성능이 저조하다는 것을 보여줍니다. 깨끗한 텍스트와 노이즈가 있는 텍스트에서의 모델 성능을 비교함으로써, 현재 접근 방식의 한계에 대한 통찰력을 제공하고 역사적 디지털화 맥락에서 더 많은 노이즈 저항성을 갖춘 QA 시스템의 필요성을 강조합니다.

## 📝 요약

이 연구는 다국어 문서의 디지털화에서 중요한 역할을 하는 광학 문자 인식(OCR) 오류가 다국어 질문-응답(QA) 시스템에 미치는 영향을 분석합니다. 이를 위해 영어, 프랑스어, 독일어로 구성된 50,000개의 질문-응답 쌍을 포함하는 다국어 QA 데이터셋인 MultiOCR-QA를 소개합니다. 이 데이터셋은 다양한 수준과 유형의 OCR 노이즈가 포함된 역사적 문서에서 수집되었습니다. 연구는 최신 대형 언어 모델(LLM)이 서로 다른 오류 조건에서 어떻게 성능을 발휘하는지를 평가하며, 특히 세 가지 주요 OCR 오류 유형에 중점을 둡니다. 결과적으로 QA 시스템이 OCR로 인한 오류에 매우 취약하며, 노이즈가 있는 텍스트에서 성능이 저하됨을 발견했습니다. 이를 통해 현재 접근 방식의 한계를 파악하고, 역사적 디지털화 맥락에서 더 강력한 노이즈 저항성을 갖춘 QA 시스템의 필요성을 강조합니다.

## 🎯 주요 포인트


- 1. Optical Character Recognition (OCR) 오류는 다국어 문서의 디지털화 과정에서 중요한 문제로, 특히 질문-응답(QA) 시스템의 성능에 부정적인 영향을 미친다.

- 2. 본 연구에서는 OCR로 인한 노이즈가 다국어 QA 시스템의 성능에 미치는 영향을 종합적으로 분석하였다.

- 3. 이를 위해 영어, 프랑스어, 독일어로 구성된 50,000개의 질문-응답 쌍을 포함하는 다국어 QA 데이터셋 MultiOCR-QA를 소개하였다.

- 4. 다양한 OCR 오류 조건 하에서 최신 대형 언어 모델(LLM)의 성능을 평가하였으며, QA 시스템이 OCR 오류에 매우 취약하다는 것을 발견하였다.

- 5. 깨끗한 텍스트와 노이즈가 있는 텍스트에서의 모델 성능을 비교하여 현재 접근 방식의 한계를 제시하고, 역사적 디지털화 맥락에서 더 강력한 노이즈 저항성을 가진 QA 시스템의 필요성을 강조하였다.


---

*Generated on 2025-09-22 16:34:30*