from user_service import create_user
from storage_service import upload_object, download_object
from attack_simulator import mass_download, failed_access_spam

# Create users
admin = create_user("admin_user", "admin")
normal_user = create_user("normal_user", "user")
attacker = create_user("evil_user", "attacker")

# Upload file
obj = upload_object(admin, "financial_report.csv", "high")

# Normal access
download_object(normal_user, obj.object_id)

# Simulate attack
mass_download(attacker, [obj.object_id])
failed_access_spam(attacker)

print("Simulation complete. Check system_logs.json")