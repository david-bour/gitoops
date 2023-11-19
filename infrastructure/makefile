get-argocd:
	helm repo update argo
	helm pull argo/argo-cd
	tar -xvf *.tgz
	rm -rf *.tgz

view:
	kubectl -n default get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
	kubectl port-forward service/argo-cd-argocd-server -n default 8080:443