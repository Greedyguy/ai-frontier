# Apertus: Democratizing Open and Compliant LLMs for Global Language Environments

**Korean Title:** Apertus: 글로벌 언어 환경을 위한 개방적이고 규범적인 대형 언어 모델의 민주화

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Alejandro Hernández-Cano|Alejandro Hernández-Cano]] [[authors/Alexander Hägele|Alexander Hägele]] [[authors/Allen Hao Huang|Allen Hao Huang]] [[authors/Angelika Romanou|Angelika Romanou]] [[authors/Antoni-Joan Solergibert|Antoni-Joan Solergibert]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Goldfish Objective

## 🔗 유사한 논문
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (82.3% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.0% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (81.3% similar)
- [[Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (81.3% similar)
- [[MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (80.8% similar)

## 📋 저자 정보

**Authors:** Alejandro Hernández-Cano, Alexander Hägele, Allen Hao Huang, Angelika Romanou, Antoni-Joan Solergibert, Barna Pasztor, Bettina Messmer, Dhia Garbaya, Eduard Frank Ďurech, Ido Hakimi, Juan García Giraldo, Mete Ismayilzada, Negar Foroutan, Skander Moalla, Tiancheng Chen, Vinko Sabolčec, Yixuan Xu, Michael Aerni, Badr AlKhamissi, Ines Altemir Marinas, Mohammad Hossein Amani, Matin Ansaripour, Ilia Badanin, Harold Benoit, Emanuela Boros, Nicholas Browning, Fabian Bösch, Maximilian Böther, Niklas Canova, Camille Challier, Clement Charmillot, Jonathan Coles, Jan Deriu, Arnout Devos, Lukas Drescher, Daniil Dzenhaliou, Maud Ehrmann, Dongyang Fan, Simin Fan, Silin Gao, Miguel Gila, María Grandury, Diba Hashemi, Alexander Hoyle, Jiaming Jiang, Mark Klein, Andrei Kucharavy, Anastasiia Kucherenko, Frederike Lübeck, Roman Machacek, Theofilos Manitaras, Andreas Marfurt, Kyle Matoba, Simon Matrenok, Henrique Mendoncça, Fawzi Roberto Mohamed, Syrielle Montariol, Luca Mouchel, Sven Najem-Meyer, Jingwei Ni, Gennaro Oliva, Matteo Pagliardini, Elia Palme, Andrei Panferov, Léo Paoletti, Marco Passerini, Ivan Pavlov, Auguste Poiroux, Kaustubh Ponkshe, Nathan Ranchin, Javi Rando, Mathieu Sauser, Jakhongir Saydaliev, Muhammad Ali Sayfiddinov, Marian Schneider, Stefano Schuppli, Marco Scialanga, Andrei Semenov, Kumar Shridhar, Raghav Singhal, Anna Sotnikova, Alexander Sternfeld, Ayush Kumar Tarun, Paul Teiletche, Jannis Vamvas, Xiaozhe Yao, Hao Zhao Alexander Ilic, Ana Klimovic, Andreas Krause, Caglar Gulcehre, David Rosenthal, Elliott Ash, Florian Tramèr, Joost VandeVondele, Livio Veraldi, Martin Rajman, Thomas Schulthess, Torsten Hoefler, Antoine Bosselut, Martin Jaggi, Imanol Schlag

## 📄 Abstract (원문)

We present Apertus, a fully open suite of large language models (LLMs)
designed to address two systemic shortcomings in today's open model ecosystem:
data compliance and multilingual representation. Unlike many prior models that
release weights without reproducible data pipelines or regard for content-owner
rights, Apertus models are pretrained exclusively on openly available data,
retroactively respecting robots.txt exclusions and filtering for
non-permissive, toxic, and personally identifiable content. To mitigate risks
of memorization, we adopt the Goldfish objective during pretraining, strongly
suppressing verbatim recall of data while retaining downstream task
performance. The Apertus models also expand multilingual coverage, training on
15T tokens from over 1800 languages, with ~40% of pretraining data allocated to
non-English content. Released at 8B and 70B scales, Apertus approaches
state-of-the-art results among fully open models on multilingual benchmarks,
rivalling or surpassing open-weight counterparts. Beyond model weights, we
release all scientific artifacts from our development cycle with a permissive
license, including data preparation scripts, checkpoints, evaluation suites,
and training code, enabling transparent audit and extension.

## 🔍 Abstract (한글 번역)

Apertus는 현재의 오픈 모델 생태계에서 두 가지 체계적인 결함인 데이터 준수와 다국어 표현을 해결하기 위해 설계된 완전 개방형 대형 언어 모델(LLMs) 모음입니다. 많은 이전 모델들이 재현 가능한 데이터 파이프라인 없이 또는 콘텐츠 소유자의 권리를 고려하지 않고 가중치를 공개하는 것과 달리, Apertus 모델은 공개적으로 이용 가능한 데이터만을 사용하여 사전 훈련되며, 사후적으로 robots.txt 제외 규정을 준수하고 비허용, 유해, 개인 식별 가능 콘텐츠를 필터링합니다. 기억화의 위험을 완화하기 위해, 우리는 사전 훈련 중 Goldfish 목표를 채택하여 데이터의 문자 그대로의 회상을 강하게 억제하면서도 다운스트림 작업 성능을 유지합니다. Apertus 모델은 또한 다국어 범위를 확장하여 1800개 이상의 언어에서 15T 토큰으로 훈련되며, 사전 훈련 데이터의 약 40%가 비영어 콘텐츠에 할당됩니다. 8B 및 70B 규모로 출시된 Apertus는 다국어 벤치마크에서 완전 개방형 모델 중 최첨단 결과에 접근하며, 개방형 가중치 모델과 경쟁하거나 이를 능가합니다. 모델 가중치 외에도, 우리는 데이터 준비 스크립트, 체크포인트, 평가 스위트, 훈련 코드 등 개발 주기의 모든 과학적 산출물을 허용적인 라이선스로 공개하여 투명한 감사와 확장을 가능하게 합니다.

## 📝 요약

Apertus는 데이터 준수와 다국어 표현 문제를 해결하기 위해 개발된 대형 언어 모델(LLM)입니다. 이 모델은 공개적으로 이용 가능한 데이터만을 사용하여 사전 학습되며, robots.txt 제외 규칙을 준수하고 비허가, 유해, 개인 식별 가능 콘텐츠를 필터링합니다. 데이터 암기를 줄이기 위해 Goldfish 목표를 채택하여 데이터의 정확한 회상을 억제하면서도 다운스트림 작업 성능을 유지합니다. 1800개 이상의 언어로 구성된 15조 개의 토큰을 학습하여 다국어 지원을 확장하며, 사전 학습 데이터의 약 40%는 비영어 콘텐츠에 할당되었습니다. 8B 및 70B 규모로 출시된 Apertus는 다국어 벤치마크에서 최첨단 결과에 도달하며, 모델 가중치뿐만 아니라 데이터 준비 스크립트, 체크포인트, 평가 도구 및 훈련 코드를 포함한 모든 과학적 산출물을 공개하여 투명한 감사와 확장을 가능하게 합니다.

## 🎯 주요 포인트

- 1. Apertus는 데이터 준수와 다국어 표현 문제를 해결하기 위해 설계된 대형 언어 모델(LLM)입니다.

- 2. Apertus 모델은 공개적으로 사용 가능한 데이터만을 사용하여 사전 훈련되며, robots.txt 제외 규칙을 준수하고 비허용, 유해, 개인 식별 가능 콘텐츠를 필터링합니다.

- 3. 기억화 위험을 줄이기 위해 Goldfish 목표를 채택하여 데이터의 문자 그대로 회상을 억제하면서도 다운스트림 작업 성능을 유지합니다.

- 4. Apertus 모델은 1800개 이상의 언어로 구성된 15조 개의 토큰을 사용하여 다국어 범위를 확장하며, 사전 훈련 데이터의 약 40%를 비영어 콘텐츠에 할당합니다.

- 5. 모델 가중치 외에도 데이터 준비 스크립트, 체크포인트, 평가 스위트 및 훈련 코드를 포함한 모든 과학적 산출물을 허용적인 라이선스로 공개하여 투명한 감사와 확장을 가능하게 합니다.

---

*Generated on 2025-09-20 07:40:05*