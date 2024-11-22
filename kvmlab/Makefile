.PHONY: create_vm

create_vm:
	cd kvmlab/roles && ansible-playbook -K kvm_provision.yaml -e vm=$(vm)

deploy_app: