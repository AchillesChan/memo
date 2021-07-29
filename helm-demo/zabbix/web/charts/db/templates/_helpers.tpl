{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "db.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "db.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "db.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*                                ####storageclass segment
Return  the proper Storage Class
*/}}
{{- define "db.storageClass" -}}                                                                                                                                                     
{{/*
Helm 2.11 supports the assignment of a value to a variable defined in a different scope,
but Helm 2.9 and 2.10 does not support it, so we need to implement this if-else logic.
*/}}
{{- if .Values.global -}} 
    {{- if .Values.global.storageClass -}} 
        {{- if (eq "-" .Values.global.storageClass) -}} 
            {{- printf "storageClassName: \"\"" -}} 
        {{- else }}
            {{- printf "storageClassName: %s" .Values.global.storageClass -}} 
        {{- end -}} 
    {{- else -}} 
        {{- if .Values.persistence.storageClass -}} 
              {{- if (eq "-" .Values.persistence.storageClass) -}} 
                  {{- printf "storageClassName: \"\"" -}} 
              {{- else }}
                  {{- printf "storageClassName: %s" .Values.persistence.storageClass -}} 
              {{- end -}} 
        {{- end -}} 
    {{- end -}} 
{{- else -}} 
    {{- if .Values.persistence.storageClass -}} 
        {{- if (eq "-" .Values.persistence.storageClass) -}} 
            {{- printf "storageClassName: \"\"" -}} 
        {{- else }}
            {{- printf "storageClassName: %s" .Values.persistence.storageClass -}} 
        {{- end -}} 
    {{- end -}} 
{{- end -}} 
{{- end -}} 

{{/*
Common labels
*/}}
{{- define "db.labels" -}}
helm.sh/chart: {{ include "db.chart" . }}
{{ include "db.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "db.selectorLabels" -}}
app.kubernetes.io/name: {{ include "db.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "db.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "db.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
