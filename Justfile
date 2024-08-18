# Define the paths for the mounted directories
MOUNT_L := "/run/media/jmfv/CHOCOFIFI_L"
MOUNT_R := "/run/media/jmfv/CHOCOFIFI_R"

# Command to copy main.py to both mounted directories
copy-keymap:
    @if [ -d {{MOUNT_L}} ] && [ -d {{MOUNT_R}} ]; then \
        echo "===> Copying main.py to MOUNT_L and MOUNT_R"; \
        rsync -rhu main.py {{MOUNT_L}}/main.py; \
        rsync -rhu main.py {{MOUNT_R}}/main.py; \
        sync; \
    else \
        echo "===> Error: One or both mount points do not exist."; \
        exit 1; \
    fi
