import os
import zipfile
import uuid

def generate_valid_twbx():
    base_dir = r"S:\SY\SEM 3\Internships\Skill Wallet"
    data_file = os.path.join(base_dir, "data", "cleaned", "mental_health_student_ecosystem_cleaned.csv")
    internships_dir = r"S:\SY\SEM 3\Internships"
    
    csv_name = "mental_health_student_ecosystem_cleaned.csv"

    # Generate 16 distinct RFC-compliant hex UUIDs
    # 8 for worksheets, 8 for windows
    ws_uuids = [f"{{{str(uuid.uuid4()).upper()}}}" for _ in range(8)]
    win_uuids = [f"{{{str(uuid.uuid4()).upper()}}}" for _ in range(8)]

    xml_content = f"""<?xml version='1.0' encoding='utf-8' ?>
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
      <aliases enabled='yes' />
      <column caption='User ID' datatype='string' name='[User ID]' role='dimension' type='nominal' />
      <column caption='Age' datatype='integer' name='[Age]' role='measure' type='quantitative' />
      <column caption='Gender' datatype='string' name='[Gender]' role='dimension' type='nominal' />
      <column caption='Occupation' datatype='string' name='[Occupation]' role='dimension' type='nominal' />
      <column caption='Stress Level' datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
      <column caption='Anxiety Score' datatype='integer' name='[Anxiety Score]' role='measure' type='quantitative' />
      <column caption='Depression Score' datatype='integer' name='[Depression Score]' role='measure' type='quantitative' />
      <column caption='Sleep Quality' datatype='string' name='[Sleep Quality]' role='dimension' type='nominal' />
      <column caption='Daily Screen Time (hrs)' datatype='real' name='[Daily Screen Time (hrs)]' role='measure' type='quantitative' />
      <column caption='Physical Activity Level' datatype='string' name='[Physical Activity Level]' role='dimension' type='nominal' />
      <column caption='Social Interaction Score' datatype='integer' name='[Social Interaction Score]' role='measure' type='quantitative' />
      <column caption='Mental Health History' datatype='string' name='[Mental Health History]' role='dimension' type='nominal' />
      <column caption='Therapy Type' datatype='string' name='[Therapy Type]' role='dimension' type='nominal' />
      <column caption='Intervention Duration (weeks)' datatype='integer' name='[Intervention Duration (weeks)]' role='measure' type='quantitative' />
      <column caption='Progress Score' datatype='integer' name='[Progress Score]' role='measure' type='quantitative' />
      <column caption='Medication Usage' datatype='string' name='[Medication Usage]' role='dimension' type='nominal' />
      <column caption='Support System Strength' datatype='string' name='[Support System Strength]' role='dimension' type='nominal' />
      <column caption='Work-Life Balance Score' datatype='integer' name='[Work-Life Balance Score]' role='measure' type='quantitative' />

      <column caption='High Stress Poor Sleep Flag' datatype='integer' name='[Calculation_HighStress_PoorSleep]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='IF [Stress Level] = &quot;High&quot; AND [Sleep Quality] = &quot;Poor&quot; THEN 1 ELSE 0 END' />
      </column>
      <column caption='Active Therapy Flag' datatype='integer' name='[Calculation_Active_Therapy]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='IF [Therapy Type] != &quot;No Therapy&quot; THEN 1 ELSE 0 END' />
      </column>
    </datasource>
  </datasources>

  <worksheets>
    <!-- Worksheet 1: Stress Level Distribution -->
    <worksheet name='Stress Level Distribution'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
            <column datatype='string' name='[User ID]' role='dimension' type='nominal' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[ctd:User ID:qk]</rows>
        <cols>[federated.main_data].[none:Stress Level:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[0]}' />
    </worksheet>

    <!-- Worksheet 2: Stress Level vs Anxiety Score -->
    <worksheet name='Stress Level vs Anxiety Score'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Anxiety Score]' role='measure' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[avg:Anxiety Score:qk]</rows>
        <cols>[federated.main_data].[none:Stress Level:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[1]}' />
    </worksheet>

    <!-- Worksheet 3: Stress Level vs Depression Score -->
    <worksheet name='Stress Level vs Depression Score'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Depression Score]' role='measure' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[avg:Depression Score:qk]</rows>
        <cols>[federated.main_data].[none:Stress Level:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[2]}' />
    </worksheet>

    <!-- Worksheet 4: Gender Mental Health Comparison -->
    <worksheet name='Gender Mental Health Comparison'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Gender]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Anxiety Score]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Depression Score]' role='measure' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[avg:Anxiety Score:qk]</rows>
        <cols>[federated.main_data].[none:Gender:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[3]}' />
    </worksheet>

    <!-- Worksheet 5: Sleep Quality vs Stress Level -->
    <worksheet name='Sleep Quality vs Stress Level'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Sleep Quality]' role='dimension' type='nominal' />
            <column datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
            <column datatype='string' name='[User ID]' role='dimension' type='nominal' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
            <encodings>
              <color column='[federated.main_data].[none:Stress Level:nk]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.main_data].[ctd:User ID:qk]</rows>
        <cols>[federated.main_data].[none:Sleep Quality:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[4]}' />
    </worksheet>

    <!-- Worksheet 6: Screen Time vs Stress Level -->
    <worksheet name='Screen Time vs Stress Level'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Stress Level]' role='dimension' type='nominal' />
            <column datatype='real' name='[Daily Screen Time (hrs)]' role='measure' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[avg:Daily Screen Time (hrs):qk]</rows>
        <cols>[federated.main_data].[none:Stress Level:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[5]}' />
    </worksheet>

    <!-- Worksheet 7: Mental Health History Prevalence -->
    <worksheet name='Mental Health History Prevalence'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Mental Health History]' role='dimension' type='nominal' />
            <column datatype='string' name='[User ID]' role='dimension' type='nominal' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Pie' />
            <encodings>
              <color column='[federated.main_data].[none:Mental Health History:nk]' />
            </encodings>
          </pane>
        </panes>
        <rows />
        <cols>[federated.main_data].[none:Mental Health History:nk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[6]}' />
    </worksheet>

    <!-- Worksheet 8: Ranked Therapy Efficacy -->
    <worksheet name='Ranked Therapy Efficacy'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.main_data' />
          </datasources>
          <datasource-dependencies datasource='federated.main_data'>
            <column datatype='string' name='[Therapy Type]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Progress Score]' role='measure' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
          </pane>
        </panes>
        <rows>[federated.main_data].[none:Therapy Type:nk]</rows>
        <cols>[federated.main_data].[avg:Progress Score:qk]</cols>
      </table>
      <simple-id uuid='{ws_uuids[7]}' />
    </worksheet>
  </worksheets>

  <windows>
    <window class='worksheet' name='Stress Level Distribution'>
      <cards />
      <simple-id uuid='{win_uuids[0]}' />
    </window>
    <window class='worksheet' name='Stress Level vs Anxiety Score'>
      <cards />
      <simple-id uuid='{win_uuids[1]}' />
    </window>
    <window class='worksheet' name='Stress Level vs Depression Score'>
      <cards />
      <simple-id uuid='{win_uuids[2]}' />
    </window>
    <window class='worksheet' name='Gender Mental Health Comparison'>
      <cards />
      <simple-id uuid='{win_uuids[3]}' />
    </window>
    <window class='worksheet' name='Sleep Quality vs Stress Level'>
      <cards />
      <simple-id uuid='{win_uuids[4]}' />
    </window>
    <window class='worksheet' name='Screen Time vs Stress Level'>
      <cards />
      <simple-id uuid='{win_uuids[5]}' />
    </window>
    <window class='worksheet' name='Mental Health History Prevalence'>
      <cards />
      <simple-id uuid='{win_uuids[6]}' />
    </window>
    <window class='worksheet' name='Ranked Therapy Efficacy'>
      <cards />
      <simple-id uuid='{win_uuids[7]}' />
    </window>
  </windows>
</workbook>
"""

    # Target filenames to overwrite everywhere
    twb_path = os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem_FIXED.twb")
    with open(twb_path, "w", encoding="utf-8") as f:
        f.write(xml_content)

    targets = [
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem_FIXED.twbx"),
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem_FIXED (1).twbx"),
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
        os.path.join(internships_dir, "Analysing_Mental_Health_in_Student_Ecosystem (1).twbx"),
        os.path.join(base_dir, "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
        os.path.join(base_dir, "docs", "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
        os.path.join(base_dir, "docs", "Analysing_Mental_Health_in_Student_Ecosystem_FIXED.twbx"),
        os.path.join(base_dir, "tableau", "Analysing_Mental_Health_in_Student_Ecosystem.twbx"),
    ]

    for target in targets:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(twb_path, arcname="Analysing_Mental_Health_in_Student_Ecosystem_FIXED.twb")
            zf.write(data_file, arcname=csv_name)
        print(f"Generated valid TWBX: {target} ({os.path.getsize(target)} bytes)")

if __name__ == "__main__":
    generate_valid_twbx()
