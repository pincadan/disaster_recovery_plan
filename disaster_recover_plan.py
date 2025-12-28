# disaster_recovery_plan.py
import os
import logging
from datetime import datetime

class DisasterRecoveryPlan:
    def __init__(self):
        self.log_file = "disaster_recovery.log"
        self.backup_dir = "/backups"
        self.config_files = ["/etc/config", "/etc/backup.conf"]
        
    def initialize(self):
        """Initialize disaster recovery components"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        logging.info("Disaster recovery initialized")
        
    def backup_critical_data(self):
        """Create backups of critical data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{self.backup_dir}/backup_{timestamp}.tar.gz"
        
        cmd = f"tar -czf {backup_path} {' '.join(self.config_files)}"
        result = os.system(cmd)
        
        if result == 0:
            logging.info(f"Backup successful: {backup_path}")
            return backup_path
        else:
            logging.error("Backup failed")
            return None
            
    def restore_from_backup(self, backup_path):
        """Restore system from backup"""
        if not os.path.exists(backup_path):
            logging.error("Backup file not found")
            return False
            
        cmd = f"tar -xzf {backup_path} -C /"
        result = os.system(cmd)
        
        if result == 0:
            logging.info("Restore successful")
            return True
        else:
            logging.error("Restore failed")
            return False

if __name__ == "__main__":
    drp = DisasterRecoveryPlan()
    drp.initialize()
    
    # Create backup
    backup = drp.backup_critical_data()
    
    # Restore from backup (example)
    if backup:
        drp.restore_from_backup(backup)