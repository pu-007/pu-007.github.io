---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
categories: {{ .Page.File.Dir | path.BaseName }}
tags: [ ]
summary: ""
---

