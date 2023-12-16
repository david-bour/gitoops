get-argocd:
	helm repo update argo
	helm pull argo/argo-cd
	tar -xvf *.tgz
	rm -rf *.tgz

install:
	helm install --create-namespace -n argocd argocd ./argo-cd

view:
	kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
	kubectl port-forward service/argocd-server -n argocd 8080:443
