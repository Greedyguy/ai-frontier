# Frustratingly Easy Data Augmentation for Low-Resource ASR

**Korean Title:** 저자원이 적은 ASR를 위한 좌절스럽도록 쉬운 데이터 증강

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Low-resource ASR|Low-resource ASR]] [[keywords/specific/Data Augmentation|Data Augmentation]] [[keywords/broad/Automatic Speech Recognition|Automatic Speech Recognition]] [[keywords/broad/Text-to-Speech|Text-to-Speech]] [[keywords/unique/Gloss-based Replacement|Gloss-based Replacement]] [[categories/cs.CL|cs.CL]] [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (84.0% similar) [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (82.9% similar) [[2025-09-19/Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Data Augmentation
**🔬 Broad Technical**: Automatic Speech Recognition, Text-to-Speech
**⭐ Unique Technical**: Gloss-based Replacement
## 🔗 유사한 논문
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (84.0% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (82.9% similar)
- [[2025-09-19/Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (82.2% similar)
- [[2025-09-17/Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications_20250917|Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications]] (81.3% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025 Towards Uncertainty Aware Arabic Readability Assessment]] (81.2% similar)


**ArXiv ID**: [2509.15373](https://arxiv.org/abs/2509.15373)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15373.pdf)


**ArXiv ID**: [2509.15373](https://arxiv.org/abs/2509.15373)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15373.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Data Augmentation, Wav2Vec2-XLSR-53
**⭐ Unique Technical**: Gloss-based Replacement
**🔬 Broad Technical**: Automatic Speech Recognition, Text-to-Speech

## 🏷️ 추출된 키워드



`Automatic Speech Recognition` • 

`Text-to-Speech` • 

`Data Augmentation` • 

`Gloss-based Replacement` • 

`Low-resource ASR`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15373v1 Announce Type: new 
Abstract: This paper introduces three self-contained data augmentation methods for low-resource Automatic Speech Recognition (ASR). Our techniques first generate novel text--using gloss-based replacement, random replacement, or an LLM-based approach--and then apply Text-to-Speech (TTS) to produce synthetic audio. We apply these methods, which leverage only the original annotated data, to four languages with extremely limited resources (Vatlongos, Nashta, Shinekhen Buryat, and Kakabe). Fine-tuning a pretrained Wav2Vec2-XLSR-53 model on a combination of the original audio and generated synthetic data yields significant performance gains, including a 14.3% absolute WER reduction for Nashta. The methods prove effective across all four low-resource languages and also show utility for high-resource languages like English, demonstrating their broad applicability.

## 🔍 Abstract (한글 번역)

arXiv:2509.15373v1 발표 유형: 신규  
초록: 이 논문은 자원이 부족한 자동 음성 인식(ASR)을 위한 세 가지 독립적인 데이터 증강 방법을 소개합니다. 우리의 기법은 먼저 글로스 기반 대체, 무작위 대체, 또는 대형 언어 모델(LLM) 기반 접근 방식을 사용하여 새로운 텍스트를 생성한 다음, 텍스트를 음성으로 변환(TTS)하여 합성 오디오를 생성합니다. 우리는 이러한 방법을 원래 주석이 달린 데이터만을 활용하여 자원이 극히 제한된 네 개의 언어(Vatlongos, Nashta, Shinekhen Buryat, Kakabe)에 적용합니다. 원본 오디오와 생성된 합성 데이터를 결합하여 사전 학습된 Wav2Vec2-XLSR-53 모델을 미세 조정한 결과, Nashta 언어에서 14.3%의 절대 WER 감소를 포함하여 상당한 성능 향상을 얻었습니다. 이 방법들은 네 개의 자원 부족 언어 모두에 효과적이며, 영어와 같은 자원이 풍부한 언어에도 유용성을 보여주어 광범위한 적용 가능성을 입증합니다.

## 📝 요약

이 논문은 자원이 부족한 자동 음성 인식을 위한 세 가지 데이터 증강 방법을 소개합니다. 이 방법들은 새로운 텍스트를 생성한 후, 이를 음성 합성(TTS)을 통해 오디오로 변환합니다. 네 가지 자원이 매우 제한된 언어(Vatlongos, Nashta, Shinekhen Buryat, Kakabe)에 적용한 결과, 사전 학습된 Wav2Vec2-XLSR-53 모델을 원본 오디오와 합성 데이터를 결합하여 미세 조정하면 성능이 크게 향상되었습니다. 특히 Nashta 언어의 경우 14.3%의 절대 WER 감소를 보였습니다. 이 방법들은 모든 저자원 언어에서 효과적이며, 영어와 같은 고자원 언어에도 적용 가능성을 보여주었습니다.

## 🎯 주요 포인트


- 1. 본 논문은 저자들이 제안한 세 가지 독립적인 데이터 증강 기법을 통해 저자원이 자동 음성 인식(ASR) 성능을 향상시키는 방법을 소개합니다.

- 2. 제안된 기법은 글로스 기반 대체, 무작위 대체, LLM 기반 접근법을 사용하여 새로운 텍스트를 생성하고, 이를 텍스트-음성 변환(TTS)으로 합성 오디오를 생성합니다.

- 3. 이 방법들은 제한된 자원을 가진 네 개의 언어(Vatlongos, Nashta, Shinekhen Buryat, Kakabe)에 적용되며, Nashta 언어에서 14.3%의 절대 WER 감소를 포함한 성능 향상을 보여줍니다.

- 4. 제안된 기법은 저자원 언어뿐만 아니라 영어와 같은 고자원 언어에도 효과적이며, 광범위한 적용 가능성을 나타냅니다.


---

*Generated on 2025-09-22 16:20:52*