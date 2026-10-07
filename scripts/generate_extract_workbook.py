import zipfile
import os
import uuid

def main():
    base_dir = r"S:\SY\SEM 3\Internships\Skill Wallet"
    data_file = os.path.join(base_dir, "data", "cleaned", "mental_health_student_ecosystem_cleaned.csv")
    internships_dir = r"S:\SY\SEM 3\Internships"
    csv_name = "mental_health_student_ecosystem_cleaned.csv"

    ws_uuids = [f"{{{str(uuid.uuid4()).upper()}}}" for _ in range(8)]
    win_uuids = [f"{{{str(uuid.uuid4()).upper()}}}" for _ in range(8)]

    sheets = [
        'Stress Level Distribution',
        'Stress Level vs Anxiety Score',
        'Stress Level vs Depression Score',
        'Gender Mental Health Comparison',
        'Sleep Quality vs Stress Level',
        'Screen Time vs Stress Level',
        'Mental Health History Prevalence',
        'Ranked Therapy Efficacy'
    ]

    ws_xml = []
    for i, name in enumerate(sheets):
        ws_xml.append(f"""    <worksheet name='{name}'>
      <table>
        <view>
          <datasources><datasource name='federated.main_data' /></datasources>
          <aggregation value='true' />
        </view>
        <style />
        <panes><pane><view><breakdown value='auto' /></view><mark class='Automatic' /></pane></panes>
        <rows />
        <cols />
      </table>
      <simple-id uuid='{ws_uuids[i]}' />
    </worksheet>""")

    win_xml = []
    for i, name in enumerate(sheets):
        win_xml.append(f"""    <window class='worksheet' name='{name}'>
      <cards />
      <simple-id uuid='{win_uuids[i]}' />
    </window>""")

    worksheets_str = '\n'.join(ws_xml)
    windows_str = '\n'.join(win_xml)

    # Added <extract count='-1' enabled='true' units='records'>
    xml = f"""<?xml version='1.0' encoding='utf-8' ?>
<workbook source-build='2024.1.0' source-platform='win' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <document-format-change-manifest>
    <AccessibleZoneTabOrder />
    <AnimationOnByDefault />
    <MarkAnimation />
    <SheetIdentifierTracking />
    <WindowsPersistSimpleIdentifiers />
  </document-format-change-manifest>
  <preferences />
  <datasources>
    <datasource caption='mental_health_student_ecosystem_cleaned' inline='true' name='federated.main_data' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='mental_health_student_ecosystem_cleaned' name='textscan.main'>
            <connection class='textscan' directory='.' filename='{csv_name}' />
          </named-connection>
        </named-connections>
      </connection>
      <extract count='-1' enabled='true' units='records'>
        <connection class='federated'>
          <named-connections>
            <named-connection caption='mental_health_student_ecosystem_cleaned' name='textscan.main'>
              <connection class='textscan' directory='.' filename='{csv_name}' />
            </named-connection>
          </named-connections>
        </connection>
      </extract>
    </datasource>
  </datasources>

  <worksheets>
{worksheets_str}
  </worksheets>

  <windows>
{windows_str}
  </windows>
</workbook>
"""

    targets = [
        os.path.join(internships_dir, "READY_TO_USE.twbx"),
        os.path.join(base_dir, "docs", "READY_TO_USE.twbx"),
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem_COMPLETE.twbx"),
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
        os.path.join(base_dir, "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
        os.path.join(base_dir, "docs", "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
    ]

    for t in targets:
        with zipfile.ZipFile(t, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(os.path.basename(t).replace(".twbx", ".twb"), xml)
            with open(data_file, "rb") as f:
                zf.writestr(csv_name, f.read())
        print(f"Generated extract-ready: {t} ({os.path.getsize(t)} bytes)")

if __name__ == '__main__':
    main()
