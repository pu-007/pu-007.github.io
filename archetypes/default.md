---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
categories: {{ .Page.File.Dir | path.BaseName }}
tags: [ ]
summary: ""
---

